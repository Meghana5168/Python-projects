import send_single_email as ss
# create bulk send email
def send_bulk_emails(emails:list, subject:str,body:str):
    for to_email in emails:
        try:
            ss.single_sender(
                to_email= to_email,
                subject= subject,
                body=body
            )
            print(f"email send successfully to {to_email}")
        except Exception as e:
            print(f"Failed ")