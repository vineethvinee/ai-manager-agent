# whatsapp_simulator/student_chat.py

from ai_logic.student_diagnosis import classify_student_response
from backend.sheets_logger import append_to_sheet

def simulate_student_flow():
    print("📱 WhatsApp Bot Simulation - Student Attendance Diagnosis\n")

    student_name = input("Enter Student Name: ")
    q1 = input("Q1: Why did you miss the class?\n> ")
    q2 = input("Q2: What could’ve helped you stay longer?\n> ")
    q3 = input("Q3: Was there any issue with the teacher/class/content?\n> ")

    combined_response = f"{q1} {q2} {q3}"

    print("\n🤖 Classifying student response using AI...\n")
    category = classify_student_response(combined_response)

    print(f"✅ Categorized as: {category}")

    append_to_sheet(student_name, combined_response, category)
    print("✅ Logged to Google Sheet!")

if __name__ == "__main__":
    simulate_student_flow()
