import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart ## this is used to combine the header parts in single code file
# sender details
Sender_email = "example@gmail.com"# your email
Sender_password = "passcode"# give your smtp passkey
#configurations
SMTP_SERVER='smtp.gmail.com' 
SMTP_PORT= 587

# single sender function
def single_sender(to_email:str,subject:str,body:str=None):
    msg= MIMEMultipart()
    msg['To']= to_email
    msg['Subject']= subject
    msg['From']= Sender_email
    msg.attach(MIMEText(body,'plain'))
    ## create server connection
    try:
        server = smtplib.SMTP(SMTP_SERVER ,SMTP_PORT)
        server.starttls() # server start sequerly
        #server login
        server.login(Sender_email,Sender_password)
        server.sendmail(Sender_email,to_email,msg.as_string())
        server.quit() # clsoe sever
        print(f"email send successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}.Error{e}")

