import smtplib
from email.message import EmailMessage

EMAIL = 'chrystian.souza.silveira@gmail.com'
PASSWORD = 'qcfbvamhgqeiqunx'

msg = EmailMessage()

msg['Subject'] = 'Envio com python'
msg['From'] = EMAIL
msg['To'] = EMAIL

msg.set_content('Você ganhou uma recarga de R$ 10.')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    smtp.send_message(msg)
