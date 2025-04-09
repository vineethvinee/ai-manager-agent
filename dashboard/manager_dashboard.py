# dashboard/manager_dashboard.py

import sys
import os

# Add project root (one level up from dashboard/) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from collections import Counter
from utils.email_alert import send_email


st.set_page_config(page_title="AI Manager Dashboard", layout="wide")

# Set up Google Sheets connection
def get_sheet_data(sheet_name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)

# Load data
student_df = get_sheet_data("AI Attendance Dashboard")
teacher_df = get_sheet_data("Teacher Check-in Log")

st.title("📊 AI Agent Dashboard - Class Manager")

# Student Insights
st.header("🎓 Student Engagement Insights")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚫 Drop-off Reasons")
    reason_counts = student_df['Category'].value_counts()
    st.bar_chart(reason_counts)

with col2:
    st.subheader("📋 Raw Attendance Logs")
    st.dataframe(student_df.tail(10), use_container_width=True)

# Teacher Insights
st.header("👩‍🏫 Teacher Preparedness Overview")

col3, col4 = st.columns(2)

with col3:
    st.subheader("✅ Check-in Status")
    status_counts = teacher_df['Category'].value_counts()
    st.bar_chart(status_counts)

with col4:
    st.subheader("📋 Raw Teacher Logs")
    st.dataframe(teacher_df.tail(10), use_container_width=True)

# Risk Flagging
st.header("⚠️ High Risk Class Sessions")

risky_students = student_df[student_df["Category"] == "Teacher-related"]
risky_teachers = teacher_df[teacher_df["Category"].isin(["Needs Support", "At Risk"])]

st.write("### 🚩 Student Complaints About Teachers")
st.dataframe(risky_students.tail(5), use_container_width=True)

st.write("### 🚩 Unprepared Teachers")
st.dataframe(risky_teachers.tail(5), use_container_width=True)


# --- Alerts & Flags ---
st.markdown("---")
st.header("🚨 Alerts & Flags")

email_triggered = False
email_body = ""

# 🔴 Alert for Teachers in Risk
risk_teachers = teacher_df[teacher_df['Category'] == 'Risk']
if len(risk_teachers) > 2:
    st.error(f"🔴 {len(risk_teachers)} teachers marked as 'Risk' — Immediate support needed!")
    email_body += f"🔴 {len(risk_teachers)} teachers marked as 'Risk'\n"
    email_triggered = True

# ⚠️ Alert for Teacher-related Student Issues
teacher_related_issues = student_df[student_df['Category'] == 'Teacher-related']
if len(teacher_related_issues) > 3:
    st.warning(f"⚠️ {len(teacher_related_issues)} students cited teacher-related reasons — Check quality!")
    email_body += f"⚠️ {len(teacher_related_issues)} students reported teacher-related issues\n"
    email_triggered = True

# ✅ Send Email Alert
if email_triggered:
    send_email("🚨 AI Manager Dashboard Alert", email_body)
