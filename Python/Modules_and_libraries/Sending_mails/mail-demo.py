import smtplib
import imghdr
from email.message import EmailMessage

EMAIL = 'EMAIL'
PASSWORD = 'PASSWORD'
RECEIVER = 'EMAIL'

# # Used for Gmail
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

# # Used for localhost (Command used - python3 -m smtpd -c DebuggingServer -n localhost:1025)
# with smtplib.SMTP('localhost', 1025) as smtp:

# # Used for Gmail (with ssl from start)
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

#     smtp.login(EMAIL, PASSWORD)

#     subject = "HELLO!!!"
#     body = "Hello Hello !!!"

#     msg = f'Subject: {subject}\n\n{body}'

#     # smtp.sedmail(SENDER, RECEIVER, msg)
#     smtp.sendmail(EMAIL, RECEIVER, msg)

# # Better way of handling this messages -
msg = EmailMessage()
msg['Subject'] = 'HELLO!!!'
msg['From'] = EMAIL
msg['To'] = RECEIVER
msg.set_content('Hello Hello !!!')

msg.add_alternative("""<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)

# # Sending an Image
# msg = EmailMessage()
# msg['Subject'] = 'HELLO!!!'
# msg['From'] = EMAIL
# msg['To'] = RECEIVER
# # # Adding Multiple Recipients
# # recipients_list = [RECEIVER, RECEIVER2]
# # msg['To'] = ', '.join(recipients_list)
# msg.set_content('Image Attached')

# # For Attaching Images
# files = ['image.png', 'image2.png']
# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name

#     msg.add_attachment(file_data, maintype='image',
#                        subtype=file_type, filename=file_name)

# # For Attaching PDF
# with open('dummy.pdf', 'rb') as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name
# msg.add_attachment(file_data, maintype='application',
#                    subtype='octect-stream', filename=file_name)

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(EMAIL, PASSWORD)
#     smtp.send_message(msg)
