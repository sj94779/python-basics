# send_email.py

import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'sj'
email['to'] = 'sj94779@gmail.com'
email['subject'] = 'Daily Update'

email.set_content('This is an automated email with the daily update.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	# using app password, not original password
	smtp.login('sj94779@gmail.com', 'vqde hedj vgkz rzyt')
	smtp.send_message(email)
	print('Email sent successfully')