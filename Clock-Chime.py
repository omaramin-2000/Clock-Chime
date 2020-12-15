# This program is a chiming clock replicating the exact Big Ben chimes.
# Can be set to ring every 15, 30, or 60 minutes.
# This code is provided under the MIT license.

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
    Hr = datetime.datetime.now().hour
    Min = datetime.datetime.now().minute
    Sec = datetime.datetime.now().second
    if Hr > 12: Hr = Hr - 12 # Subtracts 12 from the 24 hours if after12 pm, or you will get 13, 14, 15 chimes, and so on.
    if Hr == 0: Hr = 12 # 12 am is 12 chimes.
    # Only chimes if in the first 10 seconds of a minute, so this avoids a repeated chiming bug if the chime 
    # ends before the minute of 0, 15, 30, 45 passes.
    if 0 <= Sec < 5: 
        if Min == 0:
            playsound('Hour Chime.mp3')
            for y in range(Hr):
                playsound('Hour Strike.mp3')
        if x == 15 and Min == 15:
            playsound('Quarter Hour Chime.mp3')
        if x in [15, 30] and Min == 30:
            playsound('Half Hour Chime.mp3')
        if x == 15 and Min == 45:
            playsound('3 Quarter Hour Chime.mp3')
    time.sleep(1) # runs the look once a second only to save CPU and battery
