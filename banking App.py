import filestore
import time
import datetime
import requests
from bs4 import BeautifulSoup


#This is the function that is called at the beginning of the program
def ourbank():
    print ("Welcome to Our Bank, We care for you\n")
    prompt = int(raw_input("""To open a new bank account, Press 1\n"""+
                        """To access your existing account & transact press 2\n"""))
    if prompt==1:
        cus = BankAccount() # creates a new customer profile
    elif prompt==2:
        cus = ReturnCustomer() # checks for existing customer
    else:
        print "You have pressed the wrong key, please try again"
        ourbank()



# class for creating an instance of a new back account and other default bank functions
class BankAccount:
    """
    Class for a bank account
    """
    type="Normal Account"

    def __init__(self):
        ##calls functions in the module filestore
        self.username, self.userpassword, self.balance=filestore.cusaccountcheck()
        print ("Thank you %s, your account is set up and ready to use,\n a 100 dollars has been credited to your account" %self.username)
        time.sleep(2)
        self.user_functions()

    def user_functions(self):
        print("\n\nTo access any function below, enter the corresponding key")
        print ("""To:
                    check Balance, press B.
                    deposit cash,  press D.
                    withdraw cash, press W.
                    Delete account press X.
                    Deposit bill press Y.
                    
                    exit service,  press E\n
                    :"""),
        ans=raw_input("").lower()
        if ans=='b':
            ##passcheck function confirms stored password with user input
            self.pass_check()
            self.check_balance()
        elif ans == 'd':
            self.pass_check()
            self.deposit_cash()
        elif ans == 'w':
            self.pass_check()
            self.withdraw_cash()
        elif ans == 'y':
            self.pass_check()
            self.deposit_bill()
        elif ans == 'p':
            self.pass_check()
            self.compare_acount()

        elif ans == 'x':
            print ("%s, your account is being deleted"%self.username)
            time.sleep(1)
            print ("work in progress")
            time.sleep(1)
            filestore.delete_account(self.username)
            print ("Your account has been successfuly deleted, goodbye")
        elif ans == 'e':
            print ("Thank you for using Our Bank Services")
            time.sleep(1)
            print ("Goodbye %s" %self.username)
            exit()

        else:
            print "No function assigned to this key, please try again"
            self.user_functions()

    def check_balance(self):
        date=datetime.date.today()
        date=date.strftime('%d-%B-%Y')
        self.working()
        print ("Your account balance as at {} is {}").format(date, self.balance)
        self.transact_again()

    def withdraw_cash(self):
        amount=float(raw_input("::\n Please enter amount to withdraw\n: "))
        self.balance-=amount
        self.working()
        print ("Your new account balance is %.2f" %self.balance)
        print ("::\n")
        filestore.bal_update(self.username, -amount)
        self.transact_again()

    def deposit_cash(self):
        amount=float(raw_input("::\nPlease enter amount to be deposited\n: "))
        self.balance+=amount
        self.working()
        print ("Your new account balance is %.2f" %self.balance)
        print ("::\n")
        filestore.bal_update(self.username, amount)
        self.transact_again()

    def deposit_bill(self):
        billamount= float(raw_input("::\nPlease enter amount to be deposited for bill\n: "))
        self.balance-=billamount
        self.working()

        print ("After paying bill amount ,Your balance is %.2f:" %self.balance)
        self.transact_again()

    def compare_acount(self):

        print "Compare which amount is larger :::"
        if self.balance > self.deposit_cash():
            print ("your balance amount is greater then your deposit cash I-E :"+self.balance)
        elif self.balance < self.deposit_cash():
            print("Your deposite cash is greater then Your balance amount I-E :"+self.depositcash())
        elif self.balance == self.deposit_cash():
            print("Your both amounts are equal so your total amount is SO ADD BOTH ::")
            print(self.balance+self.deposit_cash())

    def transact_again(self):
        ans=raw_input("Do you want to do any other transaction? (y/n)\n").lower()
        self.working()
        if ans=='y':
            self.user_functions()
        elif ans=='n':
            print ("Thank you for using Our Bank we value you. Have a good day")
            time.sleep(1)
            print ("Goodbye {}").format(self.username)
            exit()
        elif ans!='y' and ans!='n':
            print "Unknown key pressed, please choose either 'N' or 'Y'"
            self.transact_again()

    def working(self):
        print("working"),
        time.sleep(1)
        print ("..")
        time.sleep(1)
        print("..")
        time.sleep(1)

    def pass_check(self):
        """prompts user for password with every transaction and counterchecks it with stored passwords"""
        b=3
        while b>0:
            ans=raw_input("Please type in your password to continue with the transaction\n: ")
            if ans==self.userpassword:
                return True


            else:
                print "That is the wrong password"
                b-=1
                print ("%d more attempt(s) remaining" %b)

        print ("Account has been freezed due to three wrong password attempts,\n contact your bank for help, bye bye")
        time.sleep(1)
        print ("...")
        time.sleep(1)
        print("...")
        time.sleep(1)

        exit()


class ReturnCustomer(BankAccount):
    type="Normal Account"
    def __init__(self):
        self.username, self.userpassword, self.balance=filestore.old_cuscheck()
        self.user_functions()



#  # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#####"
# Retreive data from Given website
choise = " "
choise= raw_input(" Enter A, B, C OR D in upper letter")


if choise == 'A'.upper():
    url = 'https://www.reddit.com/r/programming/search?q=code'
    headers= {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response= requests.get(url, headers= headers)
    response.content
    soup= BeautifulSoup(response.content)
    soup= BeautifulSoup(response.content)
    print soup.prettify()
   # All a elements
    print soup.find_all("a")
   # All heading elements
    print soup.find_all("h3")

elif choise =='B'.upper():
    url = 'https://news.ycombinator.com/'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.content
    soup = BeautifulSoup(response.content)
    soup = BeautifulSoup(response.content)
    print soup.prettify()
    # All a elements
    print soup.find_all("a")
   # All heading elements
    print soup.find_all("h3")

    url = 'https://www.theguardian.com/us/technology'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.content
    soup = BeautifulSoup(response.content)
    soup = BeautifulSoup(response.content)
    print soup.prettify()
    # All a elements
    print soup.find_all("a")
    # All headings
    print soup.find_all("h3")

elif choise =='D'.upper():
    url = 'https://www.theguardian.com/us/technology'
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response = requests.get(url, headers=headers)
    response.content
    soup = BeautifulSoup(response.content)
    soup = BeautifulSoup(response.content)
    print soup.prettify()
    # All a elements
    print soup.find_all("a")
    #All headings element
    print soup.find_all("h3")
else :
    print "You enter wrong alphabet"




#calling the function to run the program
ourbank()



