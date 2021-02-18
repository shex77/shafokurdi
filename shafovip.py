import random

import string

import itertools

import threading

import time

import sys

 

done = False

#here is the animation

def animate():

    for c in itertools.cycle(['|', '/', '-', '\\']):

        if done:

            break

        sys.stdout.write('\rloading ' + c)

        sys.stdout.flush()

        time.sleep(0.1)

    sys.stdout.write('\rReady to spam!     ')

 

t = threading.Thread(target=animate)

 

print(""" 

 

╔═══╦╗─╔╦═══╦═══╦═══╗
║╔═╗║║─║║╔═╗║╔══╣╔═╗║
║╚══╣╚═╝║║─║║╚══╣║─║║
╚══╗║╔═╗║╚═╝║╔══╣║─║║
║╚═╝║║─║║╔═╗║║──║╚═╝║
╚═══╩╝─╚╩╝─╚╩╝──╚═══╝






""")                                                                                  

A = """

 

instagram:sha_fo_ka

 

"""

print ("")

print(A)

t.start()

time.sleep(10)

done = True

 

typeU = int(input('Enter user type: '))

length = int(input('length of user: '))

file = open('usernames.txt', 'w')

 

if typeU == 4:

  user = string.ascii_lowercase + string.digits

  le = 1

  while le < length:

    file.write(''.join(random.choice(user) for i in range(4))+'\r\n')

    le += 1

elif typeU == 3:

  user = string.ascii_lowercase + string.digits

  le = 1

  while le < length:

    file.write(''.join(random.choice(user) for i in range(3))+'\r\n')

    le += 1

elif typeU == 2:

  user = string.ascii_lowercase + string.digits

  le = 1

  while le < length:

    file.write(''.join(random.choice(user) for i in range(2))+'\r\n')

    le += 1

file.close()
