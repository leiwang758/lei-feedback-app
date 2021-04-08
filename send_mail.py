import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'a2b7e244e685dd'
    password = '4e166c89b08b95'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer:{customer}</li></ul><ul><li>Dealer:{dealer}</li></ul><ul><li>Rating:{rating}</li></ul><ul><li>Comments:{comments}</li></ul>"
    sender_email = 'lei.wang2@ucalgary.ca'
    receiver_email = 'lei.wang2@ucalgary.ca'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lei Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())