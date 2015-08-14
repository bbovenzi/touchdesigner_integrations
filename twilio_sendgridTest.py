import sendgrid
from twilio.rest import TwilioRestClient 
import ftplib

email_address = 'EMAIL_ADDRESS'
phone_number = 'PHONE_NUMBER'
image_name = 'test.png'


ACCOUNT_SID = "ACCOUNTSID" #twilio account info
AUTH_TOKEN = "AUTHTOKEN" 
sg = sendgrid.SendGridClient('USERNAME', 'PASSWORD') # sendgrid account info

if email_address:

	message = sendgrid.Mail()
	message.add_to(email_address)
	message.set_subject('Example')
	message.add_attachment('image.jpeg', open('./image.jpeg', 'rb'))
	message.add_content_id('image.jpeg', 'ID_IN_HTML')
	message.set_html('<html><body>TEXT BEFORE IMAGE<img src="cid:ID_IN_HTML"></img>AFTER IMAGE</body></html>')
	message.set_from('Doe John <EMAIL_ADDRESS>')
	status, msg = sg.send(message)

elif phone_number:

	binary_name = 'STOR ' + image_name

	session = ftplib.FTP('ftp.WEBSITE','USERNAME','PASSWORD')
	session.cwd('public_html/img')
	file = open(image_name,'rb')                  # file to send
	session.storbinary(binary_name, file)     # send the file
	file.close()                                    # close file and FTP
	session.quit()

	image_url = 'WEBSITE'+image_name

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	 
	client.messages.create(
		to=phone_number, 
		from_="PHONENUMBER FROM TWILIO", 
		body="Check out this photo!",
		media_url=image_url  
	)