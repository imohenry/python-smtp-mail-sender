import smtplib
import getpass

HOST = "<your smtp host>"
PORT = 587

FROM_EMAIL = "<sender's mail>"
TO_EMAIL = "<receiver's mail>"
PASSWORD = getpass.getpass("Enter password: ")

MESSAGE = """Subject: test mail pls
this is purely a test mail, I hope this works

"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()
