# whatsapp_simulator/teacher_checkin.py

from ai_logic.teacher_checkin import classify_teacher_checkin
from backend.teacher_sheets_logger import append_teacher_checkin

def simulate_teacher_checkin():
    print("📱 WhatsApp Bot Simulation - Teacher Check-in\n")

    teacher_name = input("Enter Teacher Name: ")
    r1 = input("Q1: Are you ready for today’s class?\n> ")
    r2 = input("Q2: Have you reviewed the lesson plan?\n> ")
    r3 = input("Q3: Any blockers or support needed?\n> ")

    combined_response = f"{r1} {r2} {r3}"

    print("\n🤖 Classifying teacher check-in using AI...\n")
    classification = classify_teacher_checkin(combined_response)

    print(f"✅ Teacher Check-in Status: {classification}")
    append_teacher_checkin(teacher_name, combined_response, classification)
    print("✅ Logged to Google Sheet!")

if __name__ == "__main__":
    simulate_teacher_checkin()
