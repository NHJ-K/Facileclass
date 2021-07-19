import smtplib
from .mailcrd import *
from lmst.settings import WEBURL
def mailsender(Email,sub):
    smtpserver=smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
    link=WEBURL
    message=sub
    smtpserver.sendmail(EMAIL_HOST_USER,Email,message)
    print('mail scuusess')
    smtpserver.close()
            
    return True
            