# Importing the system date and time
import datetime, time
# Importing the playsound function to play audio files
from playsound import playsound

# Looping the program
while True:
    # Reads the number of minutes to chime that's written in the text file, by the other (GUI) program
    f = open('minutes to chime.txt', 'r')
    x = int(f.read())

    # Reads the text file that's responsible for the Chimes track that's determined by the other (GUI) program
    # Either if it's on or off
    g = open('global.txt', 'r')
    t = int(g.read())

    # Reads the starting hour chime from the text file that's determined by the (GUI) program
    s = open('a.txt', 'r')
    a = int(s.read())

    # Reads the ending hour chime from the text file that's determined by the (GUI) program
    e = open('b.txt', 'r')
    b = int(e.read())

    # Only chimes if the track is on
    if int(t) == 1 :
        # Defining the time variables
        Hr = datetime.datetime.now().hour
        Min = datetime.datetime.now().minute
        Sec = datetime.datetime.now().second
        
        n = ''
        # Determining if the number of starting hour chime is above the ending hour chime to recognize the range successfully
        if b >= a:
            if Hr in range(a, b): n = 1
        elif Hr >= a or Hr <= b: n = 1
	
        if n == 1:
            # Subtracts 12 from the 24 hours if after 12 pm, or you will get 13, 14, 15 chimes, and so on
            if Hr > 12: Hr -= 12
            # 12 am is 12 chimes
            if Hr == 0: Hr = 12
            
            # Only chimes if in the first 10 seconds of a minute, so this avoids a repeated chiming bug if the chime
            # ends before the minute of 0, 15, 30, 45 passes
            if 0 <= Sec <5:
                if Min == 0:
                    playsound('Hour Chime.mp3')
                    for y in range (Hr):
                        playsound('Hour Strike.mp3')
                if x == 15 and Min == 15:
                    playsound("Quarter Hour Chime.mp3")
                if x in [15, 30] and Min == 30:
                    playsound('Half Hour Chime.mp3')
                if x == 15 and Min == 45:
                    playsound('3 Quarter Hour Chime.mp3')

    # Runs the loop once a second only to save CPU and battery
    time.sleep(1)
    
