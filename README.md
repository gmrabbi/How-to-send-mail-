# How to Send Mail Using Python (Tkinter SMTP App)

A simple desktop application built with Python Tkinter that allows users to send emails using SMTP. The application provides a graphical user interface where users can enter sender details, recipient email, subject, and message to send emails directly from the system.

---

## Project Overview

This project demonstrates how to build a GUI-based email sending system using Python. It uses Tkinter for the graphical interface and Python’s built-in SMTP library (smtplib) to send emails through an email server such as Gmail.

The project is mainly designed for learning purposes, especially for understanding GUI development and email automation using Python.

---

## Features

- Simple and user-friendly GUI
- Send emails directly from desktop application
- Input fields for sender email and password
- Recipient email input support
- Subject and message body support
- One-click email sending system

---

## Technologies Used

Python, Tkinter, SMTP (smtplib)

---

## Project Structure

```
How-to-send-mail-/
│
├── main.py        # Main Tkinter application
└── README.md
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/gmrabbi/How-to-send-mail-.git
cd How-to-send-mail-
```

### 2. Run the application

```bash
python main.py
```

---

## SMTP Setup (Gmail)

To send emails using Gmail:

- Enable 2-Step Verification in your Google account  
- Generate an App Password  
- Use the App Password instead of your normal password in the application

---

## How It Works

- User opens the application  
- Enters sender email and password  
- Writes recipient email, subject, and message  
- Clicks Send button  
- Email is sent using SMTP server  

---

## Security Note

- Do not use your real password directly  
- Always use App Password for Gmail SMTP  
- Do not share credentials publicly  

---

## Future Improvements

- Add attachment support  
- Save email history  
- Improve UI design  
- Add contact list feature  

---

## Author

Golam Mostafa Rabby  
CSE Undergraduate Student  
Dhaka University of Engineering & Technology (DUET), Gazipur  

---

## License

This project is for educational purposes only.
