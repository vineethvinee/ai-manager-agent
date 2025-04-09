# backend/sheets_logger.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def append_to_sheet(student_name, reason_text, category):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    # Replace with your actual Google Sheet name
    sheet = client.open("AI Attendance Dashboard").sheet1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    row = [timestamp, student_name, reason_text, category]
    sheet.append_row(row)
