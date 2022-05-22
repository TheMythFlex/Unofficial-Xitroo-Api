import base64
import datetime
import random
import time
import colorama
import requests
import re
import os
from colorama import Fore
cwd = os.getcwd()
colorama.init()

def GenerateEmail(domain="random", length=18):
    global list
    if domain == "random":
        list = ["com", "fr", "org", "net"]
        random_domain = random.choice(list)
        domain = random_domain
    else:
        pass

    if domain == "com":
        pass
    else:
        if domain == "fr":
            pass
        else:
            if domain == "org":
                pass
            else:
                if domain == "net":
                    pass
                else:
                    if domain == "random":
                        pass
                    else:
                        print(f"""
{Fore.RED}
Traceback (an error has occurred):
   File "{cwd}"
     Error = random_email(18, ?)
TypeError: Wrong email domain, Available domains: [com, fr, org, net] or set argument to "random" """)
                        input()

    Random = ''.join(random.choice("qwertyuiopasdfghjklzxcvbnm123456789") for x in range(int(length)))
    return Random + "@xitroo." + domain

def FetchEmail(xitroo_email=None, subject=None, timeout=30):
    if xitroo_email == None:
        print(f"""
        {Fore.RED}
Traceback (an error has occurred):
   File "{cwd}"
     Error = get_email(xitroo_email=?)
TypeError: get_email(xitroo_email=?), Missing positional argument, xitroo_email= should have the value of the generated email. """)
        input()
    else:
        pass

    if subject == None:
            print(f"""
            {Fore.RED}
Traceback (an error has occurred):
   File "{cwd}"
     Error = get_email(subject=?)
TypeError: get_email(subject=?), Missing positional argument, subject= should have the value of the email subject received. """)
            input()
    else:
        pass

    subject_to_find = base64.b64encode(bytes(subject, 'utf-8'))
    conv_base64 = base64.b64encode(subject_to_find)
    Subject = base64.b64decode(conv_base64).decode()

    xitroo_session = requests.session()

    counter = 0

    while True:
        counter += 1
        now = datetime.datetime.now()
        b = now + datetime.timedelta(0, 600)
        timestamp = datetime.datetime.timestamp(b)

        xitroo_response = xitroo_session.get(
            "https://api.xitroo.com/v1/mails?locale=en&mailAddress=" + xitroo_email + "&mailsPerPage=25&minTimestamp=0&maxTimestamp=" + str(
                timestamp))

        if str(Subject) in xitroo_response.text:
            break

        time.sleep(1)

        if counter == timeout:
            return print(Fore.RED + "Email timeout limit has reached")
        else:
            pass

    email_id = re.findall('_id":"(.*?)"', xitroo_response.text)[0]

    data = {
        'id': email_id
    }

    email_body = xitroo_session.get("https://api.xitroo.com/v1/mail?locale=en&id={}".format(email_id), data=data)
    bodytext = re.findall('bodyText":"(.*?)"', email_body.text)[0]
    code = base64.b64decode(bodytext)
    conv_email_base64 = base64.b64encode(code)
    body = base64.b64decode(conv_email_base64).decode()
    return body















