checkpoint_auto_login 1.0

auto login script for checkpoint portal

Some checkpoint portal's have login time limit ,in our institute its about 4 hours after which it automatically log's you off. You then need to login to portal again.

=>This script intends to automate the login task for you,without you needing to manually open the browser and login.
=>Though time limit for logout may be say 4 hours,you can also make script login before 4 hour's pass,you can set the time accordingly.
IMPORTANT ,script currently works only for chrome.

This script uses:
=>SELENIUM ,for the chrome web driver.
=>CRYPTO framework for encrypting the saved credentials.

Steps :

1>run setup.py:
-set username,password.(it remains saved on your local machine).
-set time limit between login's.(default 3 hours)
2>run divy.py (make sure you have chrome installed)
YOU ARE DONE.
3>To change username or password ,run setup.py again.


Any suggestions and ideas are heartedly welcome.
