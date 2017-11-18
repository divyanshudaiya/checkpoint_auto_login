from god import *
from Crypto.Cipher import AES
import base64
import os
import time
#import the 'tkinter' module
import tkinter
#create a new window
window = tkinter.Tk()
#set the window background to hex code '#a1dbcd'
window.configure(background="#a1dbcd")
#set the window title
window.title("Checkpoint Auto Login Setup")
#set the window icon
#window.wm_iconbitmap('Icon.ico')

photo = tkinter.PhotoImage(file="cover.gif")
w = tkinter.Label(window, image=photo)
w.pack(side='right')

#create a label for the instructions
lblInst = tkinter.Label(window, text="It's a one time setup.", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
#and pack it into the window
lblInst.pack()

#create the widgets for entering a username
lblUsername = tkinter.Label(window, text="Username:", fg="#383a39", bg="#a1dbcd")
print(lblUsername )
entUsername = tkinter.Entry(window)
#and pack them into the window
lblUsername.pack()
entUsername.pack()

#create the widgets for entering a username
lblPassword = tkinter.Label(window, text="Password:", fg="#383a39", bg="#a1dbcd")
entPassword = tkinter.Entry(window,show="*")
#and pack them into to the window

lblTimer = tkinter.Label(window, text="Auto_Login_Interval:", fg="#383a39", bg="#a1dbcd")
entTimer = tkinter.Entry(window)
# root = Tk()
# E = tk.Entry(root)
# E.pack(anchor = CENTER)
# B = Button(root, text = "OK", command = close_window)
# B.pack(anchor = S)
# root.mainloop()
lblPassword.pack()
entPassword.pack()
lblTimer.pack()
entTimer.pack()

def close_window():
	data=open("data.file","w")
	username=str(entUsername.get()).rjust(16)
	#username=empty*8+username
	password=str(entPassword.get()).rjust(16)
	timer=int(entTimer.get())
	#password=empty*8+password
	cipher = AES.new(god,AES.MODE_ECB) 
	encoded = base64.b64encode(cipher.encrypt(username))

	data.write(encoded.decode()+'\n')
	#print(encoded)
	encoded = base64.b64encode(cipher.encrypt(password))
	data.write(encoded.decode()+'\n')
	if timer>4 or timer<1:
		timer=3
	print(username,password,timer)
	data.write(str(timer))
	data.close()

	window.destroy()
#create a button widget called btn
btn = tkinter.Button(window, text="Save", fg="#a1dbcd", bg="#383a39",command = close_window)
#pack the widget into the window
btn.pack()
tkinter.Label(window,justify=tkinter.LEFT, text='IMPORTANT : will work only if you have GOOGLE CHROME.\n,username => your username\n,password => your password\n,autologin=> Interval after which to run auto login(3 hrs default)(1-3 integer only)\n,\n,1) you need to start DIVY.exe on every system start,it\'s currently not scheduled to start automatically with system though you can schedule it in windowws scheduled tasks.\n2) once started ,the script runs on until you close it.\n3) your credentials remain stored locally.\n4) script will automatically connect if you connect to college WIFI or connect LAN cable.\n5) you can change credentials by re-running SETUP.EXE.\n\n\nThis was one impulsive hobby project,so not full proof.\nAny suggestions are heartldly welcome.(16ucc033@lnmiit.ac.in)\nsource code: https://github.com/divyanshudaiya/checkpoint_auto_login').pack(padx=30, pady=30)
tkinter.Label(window,justify=tkinter.LEFT, text='after clicking Save use the software by clicking on DIVY.exe (divy.py if running raw) ....thanks for using..Divyanshu Daiya').pack(padx=2, pady=30)
window.resizable(width=False, height=False)
#draw the window, and start the 'application'
window.mainloop()