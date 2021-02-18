import requests

from time import sleep

print("""

 

 

█▀ █░█ ▄▀█ █▀▀ █▀█
▄█ █▀█ █▀█ █▀░ █▄█
              

                            by @SHAFO
                            add me insta sha_fo_ka

""")

#cods----------------------------------------------------

sleep(1)

print("* This tool only works for Emails [ Gmail ] *")

print('')

target = input(" >> : ")

def check_email():

 url = "https://mmo69.com/_check_live_email/api.php?email=" +target

 headers = {

 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

 "Accept-Encoding": "gzip, deflate, br",

 "Accept-Language": "ar",

 "Connection": "keep-alive",

 "Host": "mmo69.com",

 "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

 }

 data = {"email":target}

 rr = requests.get(url, headers=headers, data=data)

 if rr.text.find("LIVE") >= 0:

     print(f"✔️ HAYA LA INSTA GRAM >> [ {target} ] ")

 else:

     print(f"✖️ NYA LA INSTA GRAM  >> [ {target} ]")

def check_instagram():

    url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"

    headers = {

        "accept": "*/*",

        "accept-encoding": "gzip,deflate,br",

        "accept-language": "ar,en-US;q=0.9,en;q=0.8",

        "content-length": "49",

        "content-type": "application/x-www-form-urlencoded",

        "origin": "https://www.instagram.com",

        "referer": "https://www.instagram.com/accounts/password/reset/",

        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",

        "x-csrftoken": "j4u26vxxC6D7eE63HhBde0ahZeN4mVfK",

        "x-ig-app-id": "936619743392459"

    }

    data = {"email_or_username":target, "recaptcha_challenge_field": ""}

    rr = requests.post(url, headers=headers, data=data)

    if rr.status_code == 200:

        print(f" ✔️ HAYA LA INSTA >> [ {target} ]")

    else:

        print(f" ✖️ NYA LA INSTA >> [ {target} ]")

check_email()

check_instagram()

sleep(2)

print("")

print("")

input("انقر فوق إدخال (enter) لإغلاق الأداة")

exit()

#end cods ----------------------------------------------------------------------------
