# Importing the whole module 
from tkinter import * 
from tkinter.ttk import *
  
# Importing the strftime function to retrieve the system's time 
from time import strftime

# Creating the tkinter window 
window = Tk()

# Adding the Title
window.title("Clock Chime")

# Icon set for program window
p1 = PhotoImage(file = 'clock-1605637-1360989.ico')
window.iconphoto(False, p1)

# Adding the Geometry 
window.geometry("300x585")

# This function is used to display time on the label
def clock(): 
    string = strftime('%H:%M:%S') 
    lbl.config(text = string) 
    lbl.after(1000, clock)

# Styling the label widget so that clock looks more attractive
lbl = Label(window, font = ('calibri', 35, 'bold'), background = 'red', foreground = 'white') 
lbl.pack(pady = 10, anchor = 'center') 
clock()

# Adding the toogle switch button to allow you turning the chimes either on, or off
switchlabel = Label(window, text = 'Chimes:', foreground= 'grey')
switchlabel.pack(pady = 3)

# Keeps track of the button state on/off 
#global is_on 
g = open('global.txt', 'r')
t = int(g.read())

if int(t) == 1: is_on = True
else: is_on = False

# Defining the switch function 
def switch(): 
    global is_on 
        
    # Determining the chimes switch is on or off 
    if is_on: 
        on_button.config(image = off) 
        is_on = False
        N = '0'
        f = open('global.txt', 'w')
        f.writelines(N)
        f.close()
    else: 
        on_button.config(image = on) 
        is_on = True
        N = '1'
        f = open('global.txt', 'w')
        f.writelines(N)
        f.close()

# Defining the selected button so it writes the button value number in the text file
def sel():    
    selection = str(i.get())
    f = open('minutes to chime.txt', 'w')
    f.writelines(selection)
    f.close()

i = IntVar()

# Defining The Images 
on = PhotoImage(file = "On.png") 
off = PhotoImage(file = "Off.png") 

if int(t) == 1: n = on
else: n = off

# Creating The switch Button 
on_button = Button(window, image = n, command = switch)
on_button.pack(pady = 15) 


# Adding the radio buttons so you can select the minutes to chime at (15, 30, or 60)
radiolabel = Label(window, text ='Minutes to chime:', foreground ='grey')
radiolabel.pack(pady = 10)

c = open('minutes to chime.txt', 'r')
m = int(c.read()) 

R15 = Radiobutton(window, text="Every 15 minutes", value=15, variable=i, command=sel)
R30 = Radiobutton(window, text="Every 30 minutes", value=30, variable=i, command=sel)
R60 = Radiobutton(window, text="Every 60 minutes", value=60, variable=i, command=sel)
i.set(m)

R15.pack(pady = 5, side = 'top', anchor = 'center')
R30.pack(pady = 5, side = 'top', anchor = 'center')
R60.pack(pady = 5, side = 'top', anchor = 'center')


# Propmts you to set the chiming hours

def save():
    f = open('a.txt', 'w')
    f.writelines(a.get())
    f.close()

    c = open('b.txt', 'w')
    c.writelines(b.get())
    c.close()

combolabel = Label(window, text= 'Set chiming hours:', foreground= 'grey')
combolabel.pack(pady= 30)

labelA = Label(window, text= 'from')
labelA.pack(pady= 3)

s = open('a.txt', 'r')
w = int(s.read())

# Adding the (start) combobox with the hours list to prompt you for selecting the hour to start chimes
a = Combobox(window)
a['values']= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
a.current(w)
a.pack(pady = 10, side = 'top', anchor = 'center')

labelB = Label(window, text= 'to')
labelB.pack(pady= 3)

e = open('b.txt', 'r')
y = int(e.read())

# Adding the (end) combobox with the hours list to prompt you for selecting the hour to end chimes
b = Combobox(window)
b['values']= (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
b.current(y)
b.pack(pady = 10, side = 'top', anchor = 'center')

x = Button(window, text = 'Save', command = save)
x.pack(pady = 10, anchor = 'center')
    
# Executing the tkinter 
window.mainloop()
