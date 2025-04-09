# 📚 AI Agent for Classroom Management

An AI-powered manager agent that simulates WhatsApp check-ins with students, identifies drop-off reasons, and alerts class managers to take action — all via automated dashboards and email alerts.

---

## 🔧 Features
- Simulated student interaction via WhatsApp interface
- GPT-powered classification of student responses
- Data logging into Google Sheets
- Streamlit dashboard for class manager
- Email alerts for teacher/content issues

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/your-username/ai-manager-agent.git
cd ai-manager-agent
pip install -r requirements.txt
streamlit run dashboard/manager_dashboard.py

**Folder Structure:**

ai-manager-agent/
├── ai_logic/
│   └── student_diagnosis.py
├── backend/
│   ├── sheets_logger.py
│   └── email_alert.py
├── dashboard/
│   └── manager_dashboard.py
├── whatsapp_simulator/
│   └── student_chat.py
├── credentials/
│   └── service_account.json
├── .env
└── requirements.txt

**👨‍💻 Built With:**

*. Python
*. OpenAI API (GPT-4)
*. Google Sheets API (via gspread)
*. Streamlit
*. smtplib (Email)
