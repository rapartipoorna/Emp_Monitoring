import email_listener

# Set your email, password, what folder you want to listen to, and where to save attachments
email = "poornaraparti5@gmail.com"
app_password = "bzttdoqevpvusgtm"
folder = "Inbox"
attachment_dir = "attachements"
el = email_listener.EmailListener(email, app_password, folder, attachment_dir)

# Log into the IMAP server
el.login()
print(1)
# Get the emails currently unread in the inbox
messages = el.scrape()
print(2)
print(messages)
print(3)
# Start listening to the inbox and timeout after an hour
timeout = 60
el.listen(timeout)