import requests

from time import sleep

print("""

 

  _ _                

 |_   _/ ____|               

   | || |  __                

   | || | |_ |               

  _| || |__| |               

 |_____\_____|               

 |______|                _ _ 

  / ____|               (_) |

 | |   _  _    _ _| |

 | | |_ | '_  _ \ / _ | | |

 | |__| | | | | | | (_| | | |

  \_____|_| |_| |_|\__,_|_|_|

              

                            by @i.qpa1 

""")

#cods----------------------------------------------------

sleep(1)

print("* This tool only works for Emails [ Gmail ] *")

print('')

target = input("ادخل اسم الجميل  >> : ")

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

     print(f"✔️ الإيميل  موجد في جميل >> [ {target} ] ")

 else:

     print(f"✖️ الإيميل ليس موجد في جميل  >> [ {target} ]")

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

        print(f" ✔️ الايميل موجود في الانستقرام >> [ {target} ]")

    else:

        print(f" ✖️ الإيميل ليس موجود في الانستقرام >> [ {target} ]")

check_email()

check_instagram()

sleep(2)

print("")

print("")

input("انقر فوق إدخال (enter) لإغلاق الأداة")

exit()

#end cods ----------------------------------------------------------------------------
