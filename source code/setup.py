#!C:\ProgramData\Anaconda3\python.exe
from god import *
from Crypto.Cipher import AES
import base64
import os
import time
print("##########################################")
print("               namaskar...                ")
print("##########################################")
print("")
print("        IT's a ONE TIME ONLY SETUP        ")
print("")
print("Kindly enter username and password to use for auto login")
print("")
data=open("data.file","w")
empty=" "
username=str(input("username :")).rjust(16)
#username=empty*8+username
password=str(input("password :")).rjust(16)
#password=empty*8+password
cipher = AES.new(god,AES.MODE_ECB) 
encoded = base64.b64encode(cipher.encrypt(username))

data.write(encoded.decode()+'\n')
#print(encoded)
encoded = base64.b64encode(cipher.encrypt(password))
data.write(encoded.decode()+'\n')
os.system('cls' if os.name == 'nt' else 'clear')

print("############################################")
print("                shukriya                    ")
print("############################################")
time.sleep(1)

timer=int(input("Interval after which to run auto login(3 hrs default):"))
if timer>4 or timer<1:
	timer=3
data.write(str(timer))
data.close()
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" now use the software by clicking on SADHU.exe  ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" ")
print("the app will close in 20 sec")
print('...')
print("unitl that ,please read----")
print('')
print('1) you need to start the app ,it ain\'t acheduled to start automatically with system start.')
print('2) once started the app runs on until you close it.')
print('3) your credentials remain stored locally.')
print('4) you can change credentials by restarting SETUP.EXE')

print('')
print('thanks,jai hind')
print('')
print('......Divyanshu Daiya')
time.sleep(10)
# print(type(encoded))
# a=encoded.decode()
# #print(bytes(a))
# timer=int(input("enter the interval(in hours) after which acript should auto login (default 3 hours):"))
# if timer>4:
# 	timer=3
# data.write(str(timer))
# data.close()
# print("use the software by clicking on sadhu.exe")
# decoded = cipher.decrypt(str.encode(a))
# print (decoded.strip())