import random

database = {
    2094564220: ['Adeola', 'Adegbusi', 'adeadeola234@gmail.com', 'ZuriTraining', 0]
    }


def init():       
    print("Welcome to Bank Verathena. How May We Serve You Today?")         
    haveAccount = int(input("Do You Have an Account With Us? \nPlease Press 1 for Yes and 2 for No \n"))

    if (haveAccount == 1):               
        login()
    elif (haveAccount ==2):
         register()
    else:
        print("Invalid Selection. Please Try Again")
        init()


def login():
    print("*****************************")
    print("Welcome to the Bank Verathena login function")

    userAccountNumber = int(input("Please enter your account number\n"))
    password = input("Please enter password\n")


    for accountNumber,userDetails in database.items():
        if (accountNumber == userAccountNumber):
            if (userDetails[3] == password):
                bankOperations(userDetails)                   
    print("Invalid User Details")
    login()
       
   
def register():    
    print("*******************************")
    print("Please register for a Bank Verathena account here. It only takes a minute.")

    isPasswordStrong = False    
    email = input("Please enter your email address: \n")
    firstName = input ("Please enter your first name: \n")
    lastName = input("Please enter your last name (surname): \n")
    while isPasswordStrong == False:
        password = input("Please create a strong password, no less than 8 characters: \n")
        if (len(password) < 8):
                print("Weak Password. Please create a stronger password, no less than 8 characters\n")
        else:
                print("Password Accepted")
                isPasswordStrong = True

    accountNumber = generateAccountNumber()
    database[accountNumber] = [firstName, lastName, email, password, balance]

    print("Account successfully created")
    print("****************************")
    print("Your Account Number is %d" % accountNumber)
    print("Please keep it safe")
    print("Your Account Balance is 0")
    print("You may now proceed to the login page to make a deposit")
    print("****************************")
    login()
    

def bankOperations(user):    
    print("Welcome, %s  %s " % (user [0], user [1]))
    
    operationOption = int(input("What would you like to do today?\n Please select \n 1 for Deposit\n 2 for Withdrawal\n 3 to Logout and\n 4 to Exit\n"))    
    if (operationOption == 1):
        deposit()
    elif (operationOption == 2):
        withdraw()
    elif (operationOption == 3):
       login()
    elif (operationOption == 4):
        exit()
    else:
        print("Invalid Entry")
        bankOperations(user)


def deposit():
    isafterDepositValid = False
    for balance,userDetails in database.items():
        depositAmount = int(input("Please type a deposit amount\n"))
        print(f"Depositing {depositAmount} in account")
        balance = userDetails[4]
        balance += depositAmount
        print(user_balance(userDetails))
        print(f" Your balance is {balance}")
            
    while isafterDepositValid == False:
        afterDeposit = int(input("Would you like to perform another operation?\n Press 1 for Yes and 2 for No\n"))
        if (afterDeposit == 1):
            bankOperations(userDetails) 
        elif (afterDeposit==2):
            print("Thank you for banking with Bank Verathena. Have a nice day")
            exit()
            isafterDepositValid = True
    else:
        print("Invalid Entry")
        
        
def withdraw():
    isafterWithdrawalValid = False
    for balance,userDetails in database.items():
        withdrawalAmount = int(input("Please enter a withdrawal amount\n"))
        if (withdrawalAmount > userDetails[4]):
            print("Insufficient balance. Please enter a lower balance")
            withdraw()
    else:
        print("You have withdrawn %d" %withdrawalAmount)
        newBalance = userDetails[4]
        newBalance -= depositAmount
        print(f"Your account balance is {newBalance}")
    while isafterWithdrawalValid == False:
        afterWithdrawal = int(input("Would you like to perform another operation?\n Press 1 for Yes and 2 for No\n"))
        if (afterWithdrawal == 1):
            bankOperations(userDetails) 
        elif (afterWithdrawal==2):
            print("Thank you for banking with Bank Verathena. Have a nice day")
            exit()
            isafterWithdrawalValid = True
    else:
        print("Invalid Entry")
            

def user_balance(userDetails):
    return userDetails[4]


def logout():
    login()
    

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)
    

print(generateAccountNumber())
init()
bankOperations(user)
        
