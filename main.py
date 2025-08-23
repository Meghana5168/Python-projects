import send_single_email as ss
import send_bulk_emails as sb
#main start
if __name__== "__main__":
    print("Select type of email to send \n 1.single_email \n 2. Bulk_emails")
    choice=int(input("Please Select your type"))
    subject =input("Enter Subject : ")
    body= input("Enter Body of email :")
    if choice ==1:
        reciever_email = input("Enter Reciver email : ")
        # send single mail function call
        ss.single_sender(
            to_email=reciever_email,
            subject= subject,
            body=body
        )
    elif choice == 2:
        reciever_email_list= list(input("Enter all emails seperated by comma").split(","))
        # send bulk emails function call
        sb.send_bulk_emails(
            emails=reciever_email_list,
            subject = subject,
            body = body
        )
