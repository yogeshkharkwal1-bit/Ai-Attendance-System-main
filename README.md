# AI Attendance System

An AI-powered Attendance Management System built using **Python**, **Streamlit**, and **Supabase**. The application enables teachers to create subjects, generate secure join links and QR codes, while allowing students to register and mark attendance through facial and voice authentication.

---

##  Overview

Traditional attendance systems are time-consuming and vulnerable to proxy attendance. This project automates the entire attendance process using Artificial Intelligence and biometric authentication.

The system provides a modern web interface where teachers can manage classes and students can securely mark attendance using AI-powered verification.

---

##  Features

### Teacher Module

- Secure Teacher Login
- Create and Manage Subjects
- Generate Unique Subject Codes
- Share Join Link
- QR Code Generation for Easy Joining
- View Student List
- Track Attendance Records

###  Student Module

- Register to Subjects
- Join Class using Subject Code
- Face Registration
- Voice Registration
- AI-Based Attendance Verification
- Secure Authentication

###  AI Features

- Face Recognition
- Voice Recognition
- Face Embedding Storage
- Voice Embedding Storage
- Duplicate Attendance Prevention

---

#  Screenshots

> Add screenshots here after deployment.

Example:

```
screenshots/
├── login.png
├── teacher_dashboard.png
├── student_dashboard.png
├── qr_generation.png
├── attendance.png
```

---

#  Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### Database

- Supabase (PostgreSQL)

### AI & Machine Learning

- Face Recognition
- Voice Recognition
- NumPy
- OpenCV

### QR Code

- Segno

---

#  Project Structure

```
AI-Attendance-System
│
├── src/
│   ├── database/
│   ├── pages/
│   ├── utils/
│   ├── models/
│   └── ...
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

#  Installation

## Clone Repository

```bash
git clone https://github.com/yogeshkharkwal1-bit/Ai-Attendance-System-main.git
```

Move into project directory

```bash
cd Ai-Attendance-System-main
```

---

## Create Virtual Environment

Windows

```bash
python -m venv project
```

Activate

```bash
project\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a **.env** file.

Example:

```env
SUPABASE_URL=YOUR_SUPABASE_URL
SUPABASE_KEY=YOUR_SUPABASE_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

---

#  How It Works

### Teacher

1. Login
2. Create Subject
3. Generate Subject Code
4. Share QR Code
5. Students Join
6. View Attendance

### Student

1. Join Subject
2. Register Face
3. Register Voice
4. Verify Identity
5. Attendance Marked

---

#  Security

- Face Authentication
- Voice Authentication
- Secure Database Storage
- Unique Subject Codes
- QR Code Based Joining
- Duplicate Attendance Protection

---

#  Future Improvements

- Email Notifications
- Attendance Analytics Dashboard
- Admin Panel
- Multiple Face Detection
- Liveness Detection
- Mobile Application
- Attendance Reports (PDF & Excel)
- Teacher Analytics

---

# Requirements

- Python 3.10+
- Streamlit
- Supabase Account
- Webcam
- Microphone

---

#  Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push the branch
5. Open a Pull Request

---

# License

This project is developed for educational and research purposes.

---

#  Author

**Yogesh Singh Kharkwal**

BCA Student | AI & Python Developer

GitHub:
https://github.com/yogeshkharkwal1-bit

---

## Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further development.

---

##  Contact

For suggestions or collaboration, feel free to connect through GitHub.
