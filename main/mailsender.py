import smtplib
from .Dmail import *
from lmst.settings import WEBURL
def mailsender(res,Email,sub):
    smtpserver=smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
    link=WEBURL+res
    message=sub+link
    smtpserver.sendmail(EMAIL_HOST_USER,Email,message)
    smtpserver.close()
            
    return True
            