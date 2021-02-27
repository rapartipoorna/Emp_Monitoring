from Email_login import imapobj
category = []
for i in range(len(UIDs)):
    label_dict = imapobj.get_gmail_labels(UIDs[i])
    label = label_dict[UIDs[i]]
    if 'Starred' in str(label):
        category.append('Starred')
    elif 'Important' in str(label):
        category.append('Important')
    elif len(label) == 0:
        category.append('Inbox')
    else:
        category.append('Custom Label')