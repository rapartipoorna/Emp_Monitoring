import imapclient
import smtplib

imap_server = 'imap.gmail.com'
smtp_server = 'smtp.gmail.com'
username = 'chander.raparti@gmail.com'
password = 'dnkalqiomtuhxaud'

imapobj = imapclient.IMAPClient(imap_server, ssl=True)
imapobj.login(username, password)

smtpobj = smtplib.SMTP(smtp_server, 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login(username, password)
# smtpobj.quit()

# # disconnect from the imap server
# imapobj.logout()
