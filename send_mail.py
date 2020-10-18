import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart	
username='divya.pythonlearning@gmail.com'
password='Admin11!'
msg_str="Hi ..this is dummy mail .for python learning purpose"

def send_mail(text='Email Body',subject='Hello',from_email='Divya Bhadauria <divya.pythonlearning@gmail.com>',to_emails=None):
	 assert isintance(to_emails,list)
     #login to my SMTP server
      msg = MIMEMultipart('alternative')
      msg['From'] = from_email
      msg['To'] =", ".join(to_emails)
      server = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
      server.ehlo()
      server.starttls()
      server.login(username,password)
      server.sendmail(from_email,to_emails,msg_str)


      server.quit()
