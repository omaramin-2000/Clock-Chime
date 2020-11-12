# This program is a chiming clock replicating the exact Big Ben chimes.
# Can be set to ring every 15, 30, or 60 minutes
# This code is provided under the MIT license

import datetime
import time
from time import strftime
from playsound import playsound
print("-Every 15 minutes")
print("-Every 30 minutes")
print("-Every 60 minutes")
x = int(input("Enter number of minutes to chime at (15, 30, or 60):"))
print("Running...")
while True:
    print(strftime("%H:%M:%S"), end="", flush=x)
    print("\r", end="", flush=x)
    myHour = datetime.datetime.now().hour
    myMinute = datetime.datetime.now().minute
    mySecond = datetime.datetime.now().second
    if myHour > 12: myHour = myHour - 12 # subtracts 12 from the 24 hours if after12 pm, or you will get 13,14,15 chimes, and so on
    if myHour == 00: myHour = 12 # 12 am is 12 chimes
    # only chimes if in the first 10 seconds of a minute, so this avoids a repeated chiming bug if the chime 
    # ends before the minute of 00, 15, 30, 45 passes
    if 0 <= mySecond < 5: 
        if myMinute == 00:
            playsound('Hour Chime.mp3')
            for y in range(myHour):
                playsound('Hour Strike.mp3')
        if x == 15 and myMinute == 15:
            playsound('Quarter Hour Chime.mp3')
        if x in [15, 30] and myMinute == 30:
            playsound('Half Hour Chime.mp3')
        if x == 15 and myMinute == 45:
            playsound('3 Quarter Hour Chime.mp3')
    time.sleep(1) # runs the look once a second only to save CPU and battery
