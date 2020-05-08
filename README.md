# snbank
This task enabled me to understand how to use the python path system and using the os module, writing and reading different python functions to a text file, using the json module and many more that i learnt during the course of doint this task.
The code have a staff.txt which contains essential details of the two staffs which includes ; username, password, email and fullname.
when run the program have a staff login and close app input you can use to tell the program what you want to do.
it also had a verification line, to help verify the user login details with the staff.txt file , bring up various options the user can do after login.
After verification a session file is opened using pickle module to store up the user detail, in which the user can do three different commands; the create baank account, check account details and the logout.
if the create bank account commmand is inputed, user is allowed to create a customer account with the following details, account name,opening balance, account type and account email. After creation, an account number is given to the user, and the customer details are stored in a customer.txt file.
the check account details command, allows gthe user to see the details he created after inputing the account number of the user.
After, all these are done, the user logouts and his session file is deleted, and the program returns back to the login page, where another use can login.
