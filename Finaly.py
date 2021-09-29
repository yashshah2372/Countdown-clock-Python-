import time
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import datetime

counter = 66600
running = False

def clock():
    y = time.strftime("%H:%M:%S")
    clock_label.config(text=y)
    clock_label.after(1000, clock)


def startCountdown():
	try:
		userinput = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		messagebox.showwarning('', 'Invalid Input!')
	while userinput >-1:
		mins,secs = divmod(userinput,60) 

		hours=0
		if mins >60:

			hours, mins = divmod(mins, 60)
	
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))

		root.update()
		time.sleep(1)

		if (userinput == 0):
			messagebox.showinfo("", "Time's Up")
		userinput -= 1  

def counter_label(label): 
    def count(): 
        if running: 
            global counter 
    
            if counter==66600:             
                display="Starting..."
            else:
                stamp = datetime.fromtimestamp(counter)
                string = stamp.strftime("%H:%M:%S")
                display=string 
    
            label['text']=display   
            label.after(1000, count)  
            counter += 1
    
    count()      
    
def Start(label): 
    global running 
    running=True
    counter_label(label) 
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    

def Stop(): 
    global running 
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
    

def Reset(label): 
    global counter 
    counter=66600

    if running==False:       
        reset['state']='disabled'
        stopwatch_label['text']='Stopwatch'
    
    else:                
        stopwatch_label['text']='Starting...'

root = Tk()
root.geometry("500x350")
root.title("Countdown Clock")

root.iconbitmap("Clock.ico")
myimg = ImageTk.PhotoImage(Image.open('bg.jpg'))

bgimage = Label(root, image = myimg)
bgimage.place(x=0 , y =0)

clock_label= Label(root,font='Ariel 21', bg='#e8e4e4')
clock_label.place(x=300, y=5)
clock()

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")


fv = ("Arial",24)

hour_tf= Entry(root, width=3, font=fv, textvariable=hour)
hour_tf.place(x=280,y=70)

mins_tf= Entry(root, width=3, font=fv, textvariable=minute)
mins_tf.place(x=330,y=70)

sec_tf = Entry(root, width=3, font=fv, textvariable=second)
sec_tf.place(x=380,y=70)

start_btn = Button(root, text='START', bd='5', command= startCountdown)
start_btn.place(x = 330,y = 130)


stopwatch_label = Label(root, text="Stopwatch", fg="black", font="Verdana 28", bg='#e8e4e5') 
stopwatch_label.place(x = 250,y = 200)

start = Button(root, text='Start', width=6, command=lambda:Start(stopwatch_label)) 
start.place(x=280,y=280)

stop = Button(root, text='Stop',width=6,state='disabled', command=Stop) 
stop.place(x=330,y=280) 

reset = Button(root, text='Reset',width=6, state='disabled', command=lambda:Reset(stopwatch_label)) 
reset.place(x=380,y=280) 

root.mainloop()
