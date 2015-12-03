__author__ = 'adonets'
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class C():
def send_mail(user, pwd, recipient, subject, body):
    print 'Fuckkkkkk!'
    import smtplib
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

i=random.random()
print i
send_mail('andrywkaja@gmail.com', 'asdzxc1232', 'andrywka@ukr.net', 'Fuck the System', 'Here is random number:'+str(i)+'!!!')




#driver = webdriver.Firefox()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()