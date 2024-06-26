import smtplib

# Define your SMTP server details
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_SERVER_PORT = None  # Common port for TLS

# Define your sender email address and password
SENDER_EMAIL_ADDRESS = "sabin.shrestha.er@gmail.com"  # Replace with your email
SENDER_EMAIL_PASSWORD = "pwmb tdps sclz zthj"  # Replace with your password

# Define the receiver email address
RECEIVER_EMAIL_ADDRESS = "2005sabin24@gmail.com"  # Replace with receiver's email

# Define your subject and body for the email
subject = "Python for Automation Project Update Meeting"
body = """
Dear Students,

This is a reminder about our upcoming project update meeting for the Python for Automation course, scheduled for tomorrow at 10:00 AM.

Please ensure that you have your progress reports ready and be prepared to discuss any blockers you are facing.

Looking forward to your participation.

Best regards,
Sabin Shrestha
"""

# Construct the email message
message = f'Subject: {subject}\n\n{body}'

print("Initializing SMTP server connection...")

# Initialize the SMTP server connection
smtp = smtplib.SMTP(SMTP_SERVER, SMTP_SERVER_PORT)
print("SMTP server connection initialized.")

print("Starting TLS encryption...")
# Start TLS encryption
smtp.starttls()
print("TLS encryption started.")

print("Logging in to the SMTP server...")
# Login to the SMTP server
smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
print("Logged in to the SMTP server.")

print("Sending the email...")
# Send the email
smtp.sendmail(SENDER_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, message)
print("Email sent successfully!")

print("Closing the SMTP server connection...")
# Close the SMTP server connection
smtp.quit()
print("SMTP server connection closed.")
