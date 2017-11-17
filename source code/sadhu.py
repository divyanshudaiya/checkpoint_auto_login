#!C:\ProgramData\Anaconda3\python.exe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Crypto.Cipher import AES
import base64
from god import *
cipher = AES.new(god,AES.MODE_ECB) 
data=open("data.file","r")
record=data.read().split('\n')
usernameBytes = record[0]
passwordBytes = record[1]
time_hours=record[2]
data.close()
attempt=0

while True:
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
	print(str(attempt)+" login on "+str(localtime)+"......")
	hours_3=int(time_hours)*3600
	time.sleep(hours_3)
