# checkpoint_auto_login 1.0
auto login script for checkpoint portal

**[***STANDALONE .EXE FILE's FOR WINDOWS RELEASED.***](https://raw.githubusercontent.com/divyanshudaiya/checkpoint_auto_login/master/autoLogin_win64inst.exe)**

Some checkpoint portal's have login time limit ,in our institute its about 4 hours after which it automatically log's you off.
You then need to login to portal again.

 1. This script intends to automate the login task for you,without you
    needing to manually open the browser and login.
 2. Though time limit for logout may be say 4 hours,you can also make
    script login before 4 hour's pass,you can set the time accordingly.

----------


***IMPORTANT ,script currently works only for chrome.*** 

This script uses:

 1. SELENIUM ,for the chrome web driver.
 2. CRYPTO framework for encrypting the saved credentials.


----------


***Steps (for working with raw python files):***
1. run **setup.py**:
   - set username,password.(it remains saved on your local machine).
   - set time limit between login's.(default 3 hours)
2. run **divy.py** (make sure you have chrome installed)
   - YOU ARE DONE.
3. To change username or password ,run setup.py again.


----------


***Steps (for working with .exe files):***
1. run **setup.exe**
   - set username,password.(it reamins saved on your local machine).
   - set time limit between login's.(deafult 3 hours)
2. run **divy.exe** (make sure you have chrome installed)
   - YOU ARE DONE.
3. To change username or password ,run setup.exe again.


**Any suggestions and ideas are heartedly welcome.**

