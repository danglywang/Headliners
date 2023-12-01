import mailtrap as mt
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('MAILTRAP_TOKEN')
sender_email = "Headliners@wangify.com"

def send_message(template_id = 5313119, barber_name = "Headliners Barbershop", first_name = "User", message = "default", user_email = None):
	data = {
	'Messages': [
			{
				"From": {
					"Email": sender_email,
					"Name": "Headliners Barbershop"
				},
				"To": [
					{
						"Email": user_email,
						"Name": "User"
					}
				],
				"TemplateID": template_id,
				"TemplateLanguage": True,
				"Subject": "You have a new message from [[data:barber_name:""]]",
				"Variables": {
		"firstname": first_name,
		"barber_name": barber_name,
		"message": message
	}
			}
		]
	}
	result = mailjet.send.create(data=data)
	print (result.status_code)
	print (result.json())

	client = mt.MailtrapClient(token=token)
	client.send(mail)

