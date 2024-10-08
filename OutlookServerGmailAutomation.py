import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os
import random

#Random Number Generator
balance = random.randint(5000, 10000)

# Read the Excel file
df = pd.read_excel(r"C:\Users\Kevin\Desktop\ScriptTest.xlsx")  # Adjust path to your Excel file

# Email server details
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_user = "outlookemail"
email_password = "apppassword"

# The common message template (with placeholders)
message_template = """

Dear [Name],

I hope this message finds you well.

As part of our ongoing compliance checks and security protocols, we have identified a cryptocurrency wallet registered under your details. We would like to confirm the accuracy of this information and ensure that it aligns with your records.

Below are the details we currently have on file:

Full Name: [Name]
Email Address: [Email]
Phone Number: [PhoneNumber]
Cryptocurrency Wallet Balance: [Balance] Eur 

We kindly ask that you review the information above and confirm whether it is correct. Additionally, if you would like to access or withdraw the funds associated with this wallet, please provide us with your instructions on how you wish to proceed.

Your timely response is appreciated, as it will allow us to take the necessary steps in ensuring the safe management of your assets. Should you have any questions or need further clarification, please do not hesitate to reach out to us.

We look forward to hearing from you.

Kind regards,
Kevin Dorrian
3rd Floor Recovery Agent
Action Fraud
noreply.actionfraudd@gmail.com

Whatsapp: +46 76 055 0092

"""

# Log file path
log_file = r"C:\Users\Kevin\Desktop\LogActionFraud.txt"

# Create log file if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, 'w', encoding='utf-8') as f:  # Ensure it's created with UTF-8 encoding
        f.write("")

# Function to check if an email has already been sent
def email_already_sent(email):
    with open(log_file, 'r', encoding='utf-8') as f:  # Use 'utf-8' encoding to read the file
        sent_emails = f.read().splitlines()  # Read all the emails that have been logged
    return email in sent_emails

# Function to log an email as sent
def log_email_sent(email):
    with open(log_file, 'a', encoding='utf-8') as f:  # Use 'utf-8' encoding to append to the file
        f.write(f"{email}\n")  # Append the email address to the log

# Function to send email
def send_email(to_email, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = to_email
        msg['Subject'] = subject

        # Add message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        text = msg.as_string()
        server.sendmail(email_user, to_email, text)
        server.quit()

        # Log the sent email
        log_email_sent(to_email)
        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

# Loop through the Excel rows and send personalized emails
for index, row in df.iterrows():
    recipient = row['Email']

    # Check if the email was already sent
    if email_already_sent(recipient):
        print(f"Email to {recipient} already sent, skipping.")
        continue  # Skip this email and move to the next one

    subject = row['Subject']  # Personalized subject

    # Replace placeholders with actual values
    message = message_template.replace("[Name]", row['Name']) \
        .replace("[PhoneNumber]", str(row['Phone Number'])) \
        .replace("[Balance]", str(balance)) \
        .replace("[Email]", recipient)  # Add this line to replace the email placeholder

    send_email(recipient, subject, message)
    time.sleep(random.randint(20, 60))  # Wait for 4 minutes before sending the next email

print("All emails have been processed.")
























