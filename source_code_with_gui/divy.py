from time import sleep
import threading
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Crypto.Cipher import AES
import base64
from god import *
import requests
import warnings
warnings.filterwarnings("ignore")

serialdata = ['running...........']
data = True
globalExitFlag=0
class SensorThread(threading.Thread):
    def run(self):
        
        cipher = AES.new(god,AES.MODE_ECB) 
        data=open("data.file","r")
        record=data.read().split('\n')
        usernameBytes = record[0]
        passwordBytes = record[1]
        time_hours=record[2]
        auto_reconnect=1            #record[3]
        data.close()
        
        attempt=0
        stamp=0
        while not globalExitFlag:
            #print(globalExitFlag)
            try:
                response = requests.get('https://172.22.2.6/connect/PortalMain',verify=False)
                stamp=0
                browser = webdriver.Chrome()
                browser.get(('https://172.22.2.6/connect/PortalMain'))
                time.sleep(2)
                username = browser.find_element_by_id('LoginUserPassword_auth_username')
                time.sleep(2)
                username.send_keys(cipher.decrypt(base64.b64decode(usernameBytes)).strip().decode())
                password = browser.find_element_by_id('LoginUserPassword_auth_password')
                password.send_keys(cipher.decrypt(base64.b64decode(passwordBytes)).strip().decode())

                logInButton = browser.find_element_by_id('UserCheck_Login_Button_span')
                logInButton.click()

                time.sleep(5) 

                browser.quit()

                localtime = time.asctime( time.localtime(time.time()) ) 
                attempt+=1
                serialdata.append("divy> "+str(attempt)+" login on "+str(localtime)+"......" + "logging in as " +cipher.decrypt(base64.b64decode(usernameBytes)).strip().decode() )
                hours_3=int(time_hours)*3600
                seconds_counter=0
                while seconds_counter<hours_3 and not globalExitFlag:
                    if auto_reconnect:
                        try:
                            response = requests.get('http://www.google.com')
                        except:
                            serialdata.append('not loggged in.. retrying..' )
                            try:
                                response = requests.get('https://172.22.2.6/connect/PortalMain',verify=False)
                            except:
                                serialdata.append('you are currently not connected to college LAN/WiFi. Waiting for connection....' )
                                while True and not globalExitFlag:
                                    try:
                                        response = requests.get('https://172.22.2.6/connect/PortalMain',verify=False)
                                        serialdata.append("Connection found successfully...Logging in.." )
                                        break
                                    except:
                                        pass    
                            break
                    time.sleep(1)
                    seconds_counter+=1
            except:
                if stamp<1:
                    serialdata.append('you are currently not connected to college LAN/WiFi. Waiting for connection....' )
                    stamp=1

class Gui(object):
    def __init__(self):
        self.root = Tk()
        self.background=PhotoImage(file="divybg.gif")
        self.background_label = Label(self.root, image=self.background)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #self.root.grid(padx=20, pady=20)
        self.root.configure(background="#a1dbcd")
        self.root.title("Checkpoint Auto Loginner")
        self.photo = PhotoImage(file="cover.gif")
        self.w = Label(self.root, image=self.photo)
        self.w.pack()
        self.lblInst = Label(self.root, text="you are on the go now..", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
        self.lblInst.pack()
        self.lblInst1 = Label(self.root, text="by: Divyanshu Daiya", fg="#000000",  font=("Helvetica", 7))
        self.lblInst1.pack()
        self.lblInst2 = Label(self.root, text="source: https://github.com/divyanshudaiya/checkpoint_auto_login", fg="#000000", font=("Helvetica", 7))
        self.lblInst2.pack()
        self.S = Scrollbar(self.root)     
        self.T = Text(self.root, height=4, width=50)
        self.prev=serialdata[-1]
        self.updateGUI()
        self.readSensor()

    def run(self):
        #self.lbl.pack(padx=20, pady=20,side = 'left',fill = 'y' )
        self.btn = Button(self.root, text="  EXIT :(  ", fg="#a1dbcd", bg="#383a39",command = self.close_window)
        self.btn.pack(padx=60, pady=10)
        self.S.pack(side=RIGHT, fill=Y,pady=30)
        self.T.pack(side=LEFT, fill=Y,pady=30)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        #self.lbl.grid()
        self.T.insert(END, serialdata[-1]+"\n")
        self.T.after(1000, self.updateGUI)
        self.root.resizable(width=False, height=False)
        self.root.mainloop()

    def updateGUI(self):
        #msg = "Data is True" if data else "Data is False"
        #self.lbl["text"] += "\n"
        self.root.update()
        self.T.after(1000, self.updateGUI)

    def readSensor(self):
        if self.prev != serialdata[-1]:
            self.prev=serialdata[-1]
            self.T.insert(END, serialdata[-1]+"\n")
        self.root.update()
        self.root.after(527, self.readSensor)
    def close_window(self):
        global globalExitFlag
        self.root.destroy()
        globalExitFlag=1
        exit()
#create a button widget called btn
import inspect, os
if __name__ == "__main__":
    name=inspect.getfile(inspect.currentframe())
    if name =="divy.py" or name =="divy.exe":
        SensorThread().start()
        Gui().run()
    else:
        print("please give some credit to me @ Divyanshu Daiya,change file name to original name.")
        print("")
        print("or")
        print("")
        print("build code from source:")
        print("https://github.com/divyanshudaiya/checkpoint_auto_login")
        time.sleep(10)
    