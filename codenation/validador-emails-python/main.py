import re

def valid_email(email):
    result = re.compile(r"[\w\.\-]+@[a-zA-Z0-9]+\.([a-zA-Z0-9]{1,3})(\.[a-zA-Z0-9]{0,2}){0,1}").search(email)
    if result:
        print(email+" returned "+str(result.span()))
        if(result.span()[0]==0 and result.span()[1]==(len(email))):
            #print("Returned True")
            return True
        else:
            #print("Returned False wrong size")
            return False
    else:
        #print("Returned False no Regex")
        return False
        


def filter_email(emails):
    result = []
    for email in emails:
        if(valid_email(email)):
            result.append(email)
    return result

