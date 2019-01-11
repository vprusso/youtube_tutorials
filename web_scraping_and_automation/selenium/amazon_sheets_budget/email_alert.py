import config
import smtplib


class EmailAlert(object):
    """Class for sending email alert from slave account"""
    def __init__(self, subject, msg):

        self.subject = subject
        self.msg = msg

    def send_email(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.FROM_EMAIL_ADDRESS, config.PASSWORD)
            message = 'Subject: {}\n\n{}'.format(self.subject, self.msg)
            server.sendmail(config.FROM_EMAIL_ADDRESS,
                            config.TO_EMAIL_ADDRESS,
                            message)
            server.quit()
            print("Success: Email sent!")
        except:
            print("Email failed to send.")

