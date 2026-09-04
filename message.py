from twilio.rest import Client
import datetime

def main(to:str,fromno:str,sid:str,tocken:str,message:str)->str:
    now=datetime.datetime.now()
    account_sid = sid
    auth_token = tocken
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to,
        from_=fromno,
        body=message+"AT"+now
    )
    return message.sid
