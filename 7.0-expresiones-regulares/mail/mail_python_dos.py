#Ejemplo envio de MAIL con python 2.7 en gmail
import getpass

def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except Exception as e:
        print(e)
        print "failed to send mail"

if __name__ == '__main__':
    send_email(raw_input("user:"), getpass.getpass("passwd:"), raw_input("receptor:"), raw_input("subject:"), raw_input("body:"))
