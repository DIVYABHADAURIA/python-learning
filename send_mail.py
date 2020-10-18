import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart	
username='divya.pythonlearning@gmail.com'
password='Admin11!'
msg_str="Hi ..This is dummy mail .for python learning purpose"

def send_mail(text='Email Body',subject='Hello World',from_email='Divya Bhadauria <divya.pythonlearning@gmail.com>',to_emails=None):
	 assert isinstance(to_emails,list)
	 msg = MIMEMultipart("alternative")
	 msg['From'] = from_email
	 msg['To'] =", ".join(to_emails)
	 msg['Subject']=subject
	 text_part= MIMEText(text,'plain')
	 msg.attach(text_part)
	 html_part= MIMEText("<h1> This is heading </h1>",'html')
	 msg.attach(html_part)
	 msg_str=msg.as_string()
	 server = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
	 server.ehlo()
	 server.starttls()
	 server.login(username,password)
	 server.sendmail(from_email,to_emails,msg_str)


	 server.quit()
