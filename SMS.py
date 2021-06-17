import requests

def send_OTP(OTP,phone_num):
    url = "https://www.fast2sms.com/dev/bulk"

    #YOUR PHONE NUMBER IN PLACE OF XXXXXXXXXX

    payload = "sender_id=FSTSMS&message= OTP for smart ATM is : " + str(OTP) + " 'Do not share OTP with anyone' &language=english&route=p&numbers=XXXXXXXXXX," + str(phone_num) 

    headers = {
    'authorization': "W1dG0K3o8uQYmCiczpw9rflBtsb6xNHXIAnD7SEVkvgaPJMLyUSCc3gjLGpK0kaDyENQdTHOM4urI8zZ", 
    'Content-Type': "application/x-www-form-urlencoded", 
    'Cache-Control': "no-cache",    
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)



