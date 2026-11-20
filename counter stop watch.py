import time
from tkinter import *
from tkinter import messagebox

# creating a Tk window, its geometry and title
root = Tk()
root.geometry("300x250")
root.title("Time counter")

hour = StringVar()
minute = StringVar()
second = StringVar()
#stringvar = special variable built to connect well with widgets

hour.set("00")
minute.set("00")
second.set("00")

#input from the user
hourEntry = Entry(root, width = 3, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font =("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width = 3, font=("Arial", 18, ""), textvariable=second)
secondEntry.place(x=180, y=20)

def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
               
    except:
        print("Please input the right value")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        #divmod = dvision with quotient and remainder as well
        hours = 00
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (temp == 00):
            messagebox.showinfo("Time Countdown", "Time's up ")
 
        temp -= 1

btn = Button(root, text='Set Time Countdown', bd ='5', command=submit)
btn.place(x=70, y=120)

root.mainloop()

        
        

            
        
    


























        

