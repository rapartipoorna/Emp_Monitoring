from_addresses = []
subjects = []
dates = []
days = []
months = []
years = []
times = []
sent_received = []
unsub_links = []

for i in range(len(UIDs)):
    raw_message = imapobj.fetch(UIDs[i], ['BODY[]'])
    message = pyzmail.PyzMessage.factory(raw_message[UIDs[i]][b'BODY[]'])

    if message.get_address('from')[1] == username:
        sent_received.append('Sent')
    else:
        sent_received.append('Received')

    full_date = message.get_decoded_header('date')
    from_addresses.append(message.get_address('from'))
    subjects.append(message.get_subject(''))
    unsub_link = message.get_decoded_header('List-Unsubscribe')
    if len(str(unsub_link)) > 0 and 'mailto' in unsub_link:
        unsub_link = unsub_link.split(',')
        unsub_links.append([unsub_link[idx] for idx, s in enumerate(unsub_link) if 'mailto' in s][0])
    else:
        unsub_links.append('No unsubscribe link found')

    day = full_date.split()[0].strip(',')
    date = full_date.split()[1]
    month = full_date.split()[2]
    year = full_date.split()[3]
    time = full_date.split()[4]

    days.append(day)
    dates.append(date)
    months.append(month)
    years.append(year)
    times.append(time)