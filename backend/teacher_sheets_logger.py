# backend/teacher_sheets_logger.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def append_teacher_checkin(teacher_name, response_text, classification):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open("Teacher Check-in Log").sheet1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, teacher_name, response_text, classification]
    sheet.append_row(row)
