import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mail_content = """Hello Sir/Madam,
I m Anish Kumar jha student of B. Tech CSE.
In this mail I am sending some Resume.
Please let me know if any kind of intership available or not...
Thank You
"""
# The mail addresses and password
sender_address = 'deadlinejha@gmail.com'
sender_pass = ''
receiver_address = 'anishjhacse168@gmail.com'

# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Need Internship. Sending Resume'

# The subject line
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'pdf'))
attach_file_name = 'Resume_ANISH_KUMAR_JHA_for_Anish_Jha.pdf'
attach_file = open(attach_file_name, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)  # encode the attachment

# add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename="Resume_ANISH_KUMAR_JHA")
message.attach(payload)


# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) # use gmail with port
session.starttls() # enable security
session.login(sender_address, sender_pass) # login with mail_id and ppassword
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('SuccessFully Sent')