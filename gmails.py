import imaplib

imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)
imap_server.login("email_id","password")

imap_server.select('INBOX')

# Count the unread emails
status, response = imap_server.status('INBOX', "(UNSEEN)")
unreadcount = int(response[0].split()[2].strip(').,]'))
print unreadcount
