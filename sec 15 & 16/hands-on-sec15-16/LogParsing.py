import shutil
import os
import re
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

# Function to back up logs
def backup_logs():
    logs_dir = '/path/to/logs'
    backup_dir = f'/path/to/backup_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}'  # backup_2026-09-06_10:36:00.zip
    shutil.make_archive(backup_dir, 'zip', logs_dir)

# Function to parse logs and look for errors
def parse_logs():
    with open('system.log', 'r') as file:
        logs = file.readlines()
    
    error_logs = [log for log in logs if re.search(r'ERROR', log)]
    return error_logs

# Function to send an email alert
def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

# Main DevOps task automation function
def run_devops_tasks():
    # Step 1: Backup logs
    backup_logs()

    # Step 2: Parse logs and find errors
    error_logs = parse_logs()

    # Step 3: Send email if errors are found
    if error_logs:
        send_email('Critical Error Alert', '\n'.join(error_logs))

# Run the automation tasks
run_devops_tasks()
