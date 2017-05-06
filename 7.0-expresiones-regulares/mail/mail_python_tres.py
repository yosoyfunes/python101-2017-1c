import smtplib
from email.mime.text import MIMEText
textfile = "cuerpo.txt"
yo = "locura@extrema.com"
el = "lucas.bais@gmail.com"
with open(textfile) as fp:
    msg = MIMEText(fp.read())
    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = yo
    msg['To'] = el
    s = smtplib.SMTP('localhost', 5000)
    s.send_message(msg)
    s.quit()
