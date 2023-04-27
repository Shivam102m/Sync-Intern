import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import tkinter as tk

def generate_otp(length):
    """Generate a random OTP of the specified length."""
    digits = "0123456789"
    otp = ""
    for i in range(length):
        otp += random.choice(digits)
    return otp

def verify_otp(otp, input_otp):
    """Verify whether the input OTP matches the generated OTP."""
    if otp == input_otp :
        label3.pack()
    else:
        label4.pack()


def send_email(subject, message, from_email, to_email, smtp_server, smtp_port, username, password):
    """Send an email with the specified subject and message."""
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    body = MIMEText(message, 'html')
    msg.attach(body)
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
    print("Email Sent succesfully")


subject = "Verify your email address"
message = "Use the following OTP to verify your email address:<br><br>" 
          
otp = generate_otp(6)
#print("Generated OTP:", otp)

message += "<br><br>Your OTP is: " + otp

from_email = "moreyshivam13@gmail.com"
smtp_server = "smtp-relay.sendinblue.com"
smtp_port = 587
username = "moreyshivam13@gmail.com"
password = "xsmtpsib-3a360af7f9d09f24a29514d9b79d5152b2ab55cfb0ae84ac029226114602e15c-EHB3wyL02pMKCZVa"

def store_email():
    global to_email
    to_email = input_entry_1.get()
    instructions_label_2.pack()
    input_entry_2.pack()
    submit_button_2.pack()
    send_email(subject, message, from_email, to_email, smtp_server, smtp_port, username, password)

def store_otp():
    global input_otp
    input_otp = input_entry_2.get()
    verify_otp(otp, input_otp)

window = tk.Tk()

window.title("OTP Verification")
window.geometry('500x200')

instructions_label_1 = tk.Label(window, text="Enter Your Email")
instructions_label_1.pack()

input_entry_1 = tk.Entry(window)
input_entry_1.pack()

submit_button_1 = tk.Button(window, text="Send OTP", command=store_email)
submit_button_1.pack()

instructions_label_2 = tk.Label(window, text="Enter OTP")

input_entry_2 = tk.Entry(window)

submit_button_2 = tk.Button(window, text="Verify OTP", command=store_otp)
label3 = tk.Label(window, text="OTP Verified Successfully",font=('comic sans',15), bg="black", fg="green")
label4 = tk.Label(window, text="Wrong OTP Try again",font=('comic sans',15), bg="black", fg="red")

window.mainloop()