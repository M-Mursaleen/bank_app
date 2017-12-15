#creating empty lists everytime the program is initialized
cusnames=[]
cuspasswords=[]
cusbalance=[]

##opening the storage files to collect old customer data
namefile= open("/home/mursaleen/Desktop/Python files/cusnamefile", "r")
passfile=open("/home/mursaleen/Desktop/Python files/cuspassfile", "r")
balfile=open("/home/mursaleen/Desktop/Python files/cusbalfile", "r")

#populate the empty lists with data from storage files
#check list of customer names
for line in namefile:
        cusnames.append(line[:-1])
namefile.close()

#check list of customer passwords
for line in passfile:
        cuspasswords.append(line[:-1])
passfile.close()

#check list of customer balances
for line in balfile:
        cusbalance.append(line[:-1])
balfile.close()



def cus_account_check():
    #function creates a new user
        name=""
        pin=""
        balance = 0

        while name not in cusnames and len(name)<3:
                name=raw_input("Please type in your name for this new bank account\n")
                if name not in cusnames:
                        cusnames.append(name)
                        file_write(cusnames)
                        break
                print("Sorry, that user name is already in use")
                ans=raw_input("Are you already a member at this bank? (y/n)\n")
                if ans.lower()=='y':
                        old_cuscheck()
                else:
                        cus_account_check()

        while len(pin)<4:

                pin=raw_input("Please assign a password to this account, pin should be at least 5 characters\n")
                if len(pin)>4:
                        print "your pin has been successfully saved"
                        print "Remember to always keep your pin safe and don't disclose it to anybody"
                        cuspasswords.append(pin)
                        cusbalance.append(0)
                        balance=100.0
                        cusbalance[cusnames.index(name)]=balance
                        file_write(cuspasswords)
                        file_write(cusbalance)
                        break

                print ("Sorry, that is a short password")

        return name,pin,balance

def old_cuscheck():
        # Function to check returning customer
        name=""
        while name not in cusnames:
                name=raw_input("What is your name?\n")
                if name in cusnames:
                        username=name
                        userpassword=cuspasswords[cusnames.index(name)]
                        balance=float(cusbalance[cusnames.index(name)])
                        return username, userpassword, balance
                else:
                        print ("Sorry %s, It looks like you didn't spell you name correctly or your name is not in our records"%name)
                        again=raw_input("would like to type in your name again? (y/n)")
                        if again.lower()=='y':
                                old_cuscheck()
                        else:
                                print ("Bye bye, thank you for trying Postbank")
                                exit()

def file_write(item):
        #This function writes new data into the storage files whenever called upon.
        if item==cusnames:
                text=open("cusnamefile.txt","w")
                for i in item:
                        text.write(i+"\n")
                text.close()

        elif item==cuspasswords:
                text=open("cuspassfile.txt", "w")
                for i in item:
                        text.write(i+"\n")
                text.close()

        elif item==cusbalance:
                text=open("cusbalfile.txt", "w")
                for i in item:
                        text.write(str(i)+"\n")
                text.close()


def bal_update(ind, amount):
        #This function updates the account balance after a withdraw or deposit transaction
        accountnumber=cusnames.index(ind)
        accountbal=float(cusbalance[accountnumber])
        accountbal+=amount
        cusbalance[accountnumber]=accountbal
        text=open("cusbalfile.txt", "w")
        for i in cusbalance:
                text.write(str(i)+"\n")
        text.close()


def delete_account(name):
        #This function deletes an existing account and any data that was stored about it is cleared
        accountnumber=cusnames.index(name)
        del cusnames[accountnumber]
        file_write(cusnames)
        del cusbalance[accountnumber]
        file_write(cusbalance)
        del cuspasswords[accountnumber]
        file_write(cuspasswords)
        return None