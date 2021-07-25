import smtplib as smtp


receiver = 'harshil.patel@sakec.ac.in'

def send_email(receiver, subject, body):
    
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # subject = 'This is a subject'
    # body = 'This is the body'

    username = 'kitt30401@gmail.com'
    password = 'KNIGHTRIDER'

    server.login(username, password)
    subject = subject
    body = body
    composed_message = f"Subject: {subject}\n\n {body}"
    server.sendmail(
        from_addr=username,
        to_addrs= receiver,
        msg=composed_message
    )
    print("EMAIL SENT")
    server.quit()

# send_email('harshil.patel@sakec.ac.in', 'PLACEMENT NOTIFICATION', 'You are placed in xyz!')


