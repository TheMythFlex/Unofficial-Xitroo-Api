#On this Example we are getting a link to verify

>>> from xitroo import Api

email = Api.GenerateEmail(length=18, domain="fr")
print(email)
#>>> thisisanexample@xitroo.fr

#use this email on whatever site you want

#you need to grab the subject of the email that the website sent and place it in the function below,
#It dosent have to be the full subject just a part of it

Body = Api.FetchEmail(xitroo_email=email, subject="verify your account", timeout=15)
print(Body)
#>>> Thanks for registering please click the link below to comlpte registration
    #https://example.com/verify-user-account

# you can use regex to grab the link only from the Body, For example

link = re.findall('registration\n(.*?)', str(Body))[0]
print(link)
#>>> https://example.com/verify-user-account

#to verify the account with a link you got two options either you use selenium and open the link with chromedriver
#or send a request to that link