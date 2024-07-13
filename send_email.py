
from email import encoders, message
from email.mime.base import MIMEBase
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
def send(filename):
        from_add = "gashawgedef@gmail.com"
        to_add = "melkamu372@gmail.com"
        subject ="Today's Iphone Price list at Ebay.com"
        msg =MIMEMultipart()
        msg['From'] =from_add
        msg['To'] =to_add
        msg['Subject']=subject
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(from_add,'ugec npjo wmex oagi')
        body = "Today's Iphone price list Attached"
        msg.attach(MIMEText(body,'plain'))
        my_file = open(filename,'rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload((my_file).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition','attach;filename='+filename)
        msg.attach(part)
        message1 =msg.as_string()
        server.sendmail(from_add,to_add,message1)
        server.quit()
