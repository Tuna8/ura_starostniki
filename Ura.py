from pynput.mouse import Button, Controller
from tkinter import *
import time
import datetime
mouse = Controller()
root = Tk()
time1 = ''
clock = Label(root, font=('Ubuntu', 82, 'bold', ), fg='#c9a4a0', bg='#2b2b2b')
dan = Label(root,  font=('Ubuntu', 78 ), fg = '#d48d2c', bg='#2b2b2b')
datum = Label(root,  font=('Ubuntu', 80 ), fg = '#9ed466', bg='#2b2b2b')
clock.pack(fill = BOTH, expand=1)
dan.pack(fill = BOTH, expand = 1)
datum.pack(fill = BOTH, expand = 1)


dnevi = {0:'Ponedeljek', 1:'Torek', 2: 'Sreda', 3:'Četrtek', 4:'Petek', 5:'Sobota', 6:'Nedelja'}
def tick():
    global time1
    # get the current local time from the PC
    cas = datetime.datetime.now()
    time2 = cas.strftime('%H:%M:%S')
    # if time string has changed, update it
    datumlabel = cas.strftime('%d.%m.%Y')
    danlabel = dnevi[cas.weekday()]
    if time2 != time1:
        time1 = time2

    ura = cas.strftime('%H')
    if 6<= int(ura) < 9:
        deldneva= 'zjutraj'
    elif 9 <= int(ura) < 12 :
        deldneva = 'dopoldne'
    elif 12 <= int(ura) < 14:
        deldneva= 'opoldne'
    elif 14 <= int(ura) < 18:
        deldneva= 'popoldne'
    elif 18<= int(ura) < 21:
        deldneva= 'zvečer'
    else:
        deldneva= 'ponoči'

    datum.config(text =datumlabel)
    dan.config(text =  danlabel.upper() +"\n"+  deldneva.upper() )
    clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    mouse.scroll(0,2)
    clock.after(1000, tick)
tick()
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event:root.attributes("-fullscreen", False))
root.mainloop(  )
