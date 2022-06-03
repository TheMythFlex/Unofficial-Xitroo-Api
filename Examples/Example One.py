from xitroo import Api

email = Api.GenerateEmail(length=21, domain="random")
print(email)
#>>> thisisanexample@xitroo.com

#use this email on whatever site you want, for this example im using it on instagram

#you need to grab the subject that instagram uses in there emails and place it in the function below,
#It dosent have to be the full subject just a part of it

Body = Api.FetchEmail(xitroo_email=email, subject="your instagram code is")
print(Body)
#>>> your instagram code is 762354

# you can use regex to grab the code only from the Body, For example

code = re.findall('your instagram code is (.*?)', str(Body))[0]
print(code)
#>>> 762354