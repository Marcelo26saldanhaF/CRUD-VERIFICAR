import re

def confere_email(email):
    regra_email=re.compile("[\w]+@[\w]+\.[a-z]{2,3}[\.]?([a-z]{2})?")
    if(re.fullmatch(regra_email,email)):
        return True
    else:
        return False
