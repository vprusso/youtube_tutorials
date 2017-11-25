import smtplib

email_address = ""
password = ""

def send_email(subject, msg):
    try:  
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email_address, password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(email_address, email_address, message)
        server.quit()
        
        print('Email sent!')
    except:  
        print('Something went wrong...')
