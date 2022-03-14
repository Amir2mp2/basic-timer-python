
from tkinter import *
import time
app = Tk()
app.geometry('380x200')
app.resizable(0, 0)
app.config(bg='BLACK')
sec = StringVar()
mins = StringVar()
hrs = StringVar()
Entry(app, textvariable=sec, width=2, font=('bold' , 13)).place(x=220, y=120)
Entry(app, textvariable=mins, width=2, font=('bold' , 13)).place(x=180, y=120)
Entry(app, textvariable=hrs, width=2 , font=('bold' , 13)).place(x=142, y=120)
mins.set('00')
sec.set('00')
hrs.set('00')
app.title("TIMER")
def timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        time.sleep(1)
        app.update()
        if (times == 0):
            Label(app, text='KNOCK KNOCK TIME IS OVER', bg='RED', fg='white', font=("bold", 13), bd=5).place(x=75, y=30)
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1
Label(app,text='Set the Timer', bg ='RED' , fg = 'white', font = ("bold",20) , bd = 5).place(x=105, y=70)
Button(app, text='START', bd='2', bg='red',fg = 'white', command = timer).place(x=170, y=165)
app.mainloop()