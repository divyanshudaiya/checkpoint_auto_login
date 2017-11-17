# checkpoint Auto login 1.0

#STANDALONE EXE FILE's FOR WINDOWS RELEASED.

Some checkpoint portal's have login time limit ,in our institute its about 4 hours after which it automatically log's you off.
You then need to login to portal again.

=> This script intends to automate the login task for you,without you needing to manually open the browser and login.
=> Though time limit for logout may be say 4 hours,you can also make scipt login before 4 hour's pass,you can set the time accordingly.

IMPORTANT ,script currently works only for chrome,you need to have 

This script uses:
1> selenium ,for the chrome web driver.
2> crypto framework for encryting the saved credentials.


Steps(for working with raw python files)=>
1>run setup.py
  =>set username,password.(it reamins saved on your local machine).
  =>set time limit between login's.(deafult 3 hours)
2>run sadhu.py (make sure you have chrome installed)
  YOU ARE DONE.
3> to change username or password ,run setup.py again.

Steps(for working with .exe files) =>
1>run setup.exe
  =>set username,password.(it reamins saved on your local machine).
  =>set time limit between login's.(deafult 3 hours)
2>run sadhu.exe (make sure you have chrome installed)
  YOU ARE DONE.
3> to change username or password ,run setup.exe again.


Any suggestions and ideas are heartedly welcome.
