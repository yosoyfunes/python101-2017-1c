from ftplib import FTP
ftp = FTP('ftp.debian.org')     # connect to host, def port
ftp.login()
ftp.cwd('debian')
print(ftp.retrlines('LIST'))
status = ftp.retrbinary('RETR README', open('README', 'wb').write)
ftp.quit()
