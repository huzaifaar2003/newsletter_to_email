import smtplib
import ssl
import os

def send_mail(message, username= "automated.huzaifaar2003@gmail.com"):
    host = "smtp.gmail.com"  # NOT "smtp@gmail.com"
    port = 465
    #username = "automated.huzaifaar2003@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "automated.huzaifaar2003@gmail.com"
    context = ssl.create_default_context()
    #message = message
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        # explicit declaration of "context" argument because argument order wasn't followed
        server.login(username, password)
        server.sendmail(username, receiver, message)