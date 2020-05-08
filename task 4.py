import os
import json
Staffs =[{'Username':'david',
          'Password':'npnathan1',
          'Email':'davidgames@gmail.com',
          'Fullname': 'David Games'},
         {'Username':'nathan',
          'Password':'collins24',
          'Email':'nathansomto@gmail.com','Fullname':'Nathan Somto'}]
with open('file.txt', 'w+') as json_file:
    json.dump(Staffs,json_file)
log_in = False
log_choice= input('''Different run scenarios  Enter staff_login to login
                              Enter close_app to quit program : >''').lower()
if log_choice == 'staff_login':
    while not log_in:
        staff_user1 = str(input('Enter Staff name :')).lower()
        staff_password1 = str(input('Enter user password :')).lower()
        with open('file.txt') as file:
            user_data = json.load(file)
            print(user_data)
            for user in user_data:
                if staff_user1 == user['Username']  and staff_password1 == user['Password']:
                    log_in =True
                    print('Logged in Successfull')
                    break
            else:
                print('Invalid login')
                print('Try Again')
                staff_user1 = str(input('Enter Staff name :')).lower()
                staff_password1 = str(input('Enter user password :')).lower()
import pickle
pickle_out = open("session.pickle","wb")
staff_choice = input("1.Create bank account\n 2. Check account details\n 3. logout\n")
if staff_choice == '1':
    Account_Name = input('Account_name :')
    Opening_balance = int(input('Opening balance is : '))
    Account_type = input('Choice of Account: ')
    Account_email = input ('Account_email: ')
    s = open('customer_detail.txt', 'w+')
    s.write("Account_name: %s\n"%Account_Name)
    s.write("Opening_balance_amount: %s\n"%Opening_balance)
    s.write("Account_Type: %s\n"%Account_type)
    s.write("Account_Email:%s\n"%Account_email)
    Account_Number = int(2341098234)
    s.close()
    print (Account_Number)
staff_choice = input("1.Create bank account\n 2. Check account details\n 3. logout\n")
if staff_choice == '2':
    requested_account_number = int(input('Put in the account number:'))
    while requested_account_number == Account_Number:
        with open('customer_detail.txt') as file:
            print(file.read())
            break
            file.close()
pickle.dump(user_data,pickle_out)
pickle_out.close()
pickle_in = open("session.pickle","rb")
session = pickle.load(pickle_in)
print(session)
staff_choice = input("1.Create bank account\n 2. Check account details\n 3. logout\n")
if staff_choice == 3:
    os.remove("session.pickle")
    print('session file has been removed successfully!!')
log_choice = input('''Different run scenarios  Enter staff_login to login
                                  Enter close_app to quit program : >''').lower()
if log_choice == 'close_app':
    exit()
