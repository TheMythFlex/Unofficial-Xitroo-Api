Unofficial Xitroo Api
===============
An API for xitroo.com, Xitroo is a temporarily email service website that offers unlimited emails for free,
Unfortunately they don't have an API so i made my own Unofficial Xitroo Api and decided to share it with you guys, It can be used for websites that require to email verify to sign up and much more.

Installing
============



    pip install xitroo-api


Usage
=====

![u1](https://user-images.githubusercontent.com/93522281/171869314-37e42cc2-ac7b-42ca-b58d-e43ac7a8a3b7.png)




    >>> from xitroo import Api
    
    Api.GenerateEmail(length=18, domain="com")

    Api.FetchEmail(xitroo_email="email here", subject="subject here")

    -----------------------------------------------------------------

    GenerateEmail arguments:
    
    1 - length: is the amount of characters in the random string, it can be set to any number default is 18 characters. 
    2 - domain: xitroo has multiple domains such as [.com, .fr, .net, .org] you can chosse anyone you want or you can set it to "random".

    FetchEmail arguments:

    1 - xitroo_email: Its the email generated from [Api.GenerateEmail(length=21, domain="random")]
    2 - Subject: its from what site you used the email on, Its the subject of the email received.
    3 - Timeout: How long to wait for the email to be received, The default is 30 secends it can be set to any amount of time 


Example One
=====


![img4](https://user-images.githubusercontent.com/93522281/171868740-dce3ae71-1072-4a95-a555-e03592102eb7.png)





Example One
=====


    >>> from xitroo import Api
    
    email = Api.GenerateEmail(length=21, domain="random")
    print(email)
    >>> thisisanexample@xitroo.com

    #use this email on whatever site you want, for this example im using it on instagram

    #you need to grab the subject that instagram uses in there emails and place it in the function below,
    It dosent have to be the full subject just a part of it 

    Body = Api.FetchEmail(xitroo_email=email, subject="your instagram code is")
    print(Body)
    >>> your instagram code is 762354

    # you can use regex to grab the code only from the Body, For example
 
    code = re.findall('your instagram code is (.*?)', str(Body))[0]
    print(code)
    >>> 762354

Example Two
=====

![e2](https://user-images.githubusercontent.com/93522281/171869800-96c8f0eb-2693-49e7-bb3c-25099c2821ce.png)


    On this Example we are getting a link to verify

    >>> from xitroo import Api
    
    email = Api.GenerateEmail(length=18, domain="fr")
    print(email)
    >>> thisisanexample@xitroo.fr

    #use this email on whatever site you want

    #you need to grab the subject of the email that the website sent and place it in the function below,
    It dosent have to be the full subject just a part of it 

    Body = Api.FetchEmail(xitroo_email=email, subject="verify your account", timeout=15)
    print(Body)
    >>> Thanks for registering please click the link below to comlpte registration
        https://example.com/verify-user-account 

    # you can use regex to grab the link only from the Body, For example
 
    link = re.findall('registration\n(.*?)', str(Body))[0]
    print(link)
    >>> https://example.com/verify-user-account

    to verify the account with a link you got two options either you use selenium and open the link with chromedriver
    or send a request to that link

#Contact me on discord: Flex#8629

