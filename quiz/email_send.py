import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


outer = MIMEMultipart('alternative')
outer['Subject'] = "Verify Account For Interstellar"
outer['To'] = reciever
outer['From'] = 'interstellar@cecsummit.org'
message = """
			<h2>Hello {},</h2> 
				<h3>This is a Verification Message</h3>
				<p>Please enter the Verification code in the registration process or enter the key after logging in with
				the provided username and password</p>
				<h3>Please Do Keep this message and the verification code for further use</h3>
				<br>	
				<h3>The verification code is  {}</h3>

					<h4>Intestellar Team :)</h4>
					<br>
					 DO not Reply To this message 
				""".format(name,vericode)
HTML_BODY = MIMEText(message,'html')
outer.attach(HTML_BODY)


print "started Sending"
try:
	server = smtplib.SMTP_SSL('terminal1.veeblehosting.com',465)
	server.login('interstellar@cecsummit.org','interstellar123@')
	server.sendmail(sender, reciever,outer.as_string())
	server.quit()
	print "Sent Email"
except Exception, e:
	print e

