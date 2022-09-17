# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
# https://pypi.org/project/sendgrid/

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Sets SendGrid API Key from dotenv - Remember to replace with your API Key on .env file
load_dotenv()
account_sid = os.getenv('SENDGRID_API_KEY')

message = Mail(
    from_email='from-email@example.com',
    to_emails='to-email@example.com',
    subject='SendGrid greetings from Kirbo',
    html_content='<h1><span style="font-weight:bold;font-family:"Garamond";"><span style="color:#F700FF;">H</span><span style="color:#F801E8;">a</span><span style="color:#F902D2;">a</span><span style="color:#FA03BB;">a</span><span style="color:#FB05A5;">a</span><span style="color:#FC068E;">a</span><span style="color:#FD0778;">a</span><span style="color:#FE0861;">i</span></span></h1><br><img src="https://c.tenor.com/8eKNac12BOwAAAAC/kirby-happy.gif" width="10%"><br><br>Signing off,<br><span style="font-weight:bold;font-family:"Palatino Linotype";font-size:27px;">LG</span>>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)

    r_status = str(response.status_code)
    r_body = str(response.body)
    r_headers = str(response.headers)

    print("\nStatus Code: " + r_status + "\n")
    print("Body Response: \n" + r_body + "\n")
    print("Headers Response: \n" + r_headers)

except Exception as e:
    error = str(e.message)

    print("Error: \n" + error)
