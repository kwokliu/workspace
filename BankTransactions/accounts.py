__author__ = 'Liu'
# Python 2.7

import random, time, os, sys, re


# Account info menu
# Called when -i
# Will allow the user to choose an account by entering the number, or to quit by entering a 'q'
# Will then list account info:
# Prompt to return to the list of account holders (so the user has time to read the output)
def account_info_menu():
    again = 1
    global account_dict, menu
    while again:
        print('Info\n----')
        # Print all ac menu
        for k in menu:
            print str(k) + ") " + account_dict[menu[k]].acct_name + " " + account_dict[menu[k]].acct_number
            # prompt input from user
        print('q) uit')
        user_input = raw_input('Enter choice => ')
        if user_input == 'q':
            again = 0
            print 'Bye!'
        else:
            user_input = int(user_input)
            if menu.get(user_input) is not None:
                print '\naccount #: ' + account_dict[menu[user_input]].acct_number
                print 'name : ' + account_dict[menu[user_input]].acct_name
                print 'acct balance : ' + str(account_dict[menu[user_input]].balance) + '\n\n'
            else:
                print('Invalid input\n')


# Account history menu
# Called when -h
# Will allow the user to choose an account by entering the number, or to quit by entering a 'q'
# Prompt user select a account from menu, List all the transactions for that account
def account_history_menu():
    again = 1
    global account_dict, menu
    while again:
        print('History\n----')
        # Print all ac menu
        for k in menu:
            print str(k) + ") " + account_dict[menu[k]].acct_name + " " + account_dict[menu[k]].acct_number
            # prompt input from user
        print('q) uit')
        user_input = raw_input('Enter choice => ')
        if user_input == 'q':
            again = 0
            print 'Bye!'
        else:
            user_input = int(user_input)
            print('\n')
            if menu.get(user_input) is not None:
                for records in account_dict[menu[user_input]].trans_lis:
                    print(records)
                print('\n')
            else:
                print('Invalid input\n')


# Account Transaction menu
# Called when -t
# Display an enumerated, alphabetical list of account holder, followed by the account number
# Display option for create a new account
# Type (withdrawal or deposit), using simple keystrokes (w for or withdrawal d, followed by [enter])
def account_transaction_menu():
    again = 1
    global account_dict, menu
    while again:
        print('Transaction\n----')
        # Print all ac menu
        for k in menu:
            print str(k) + ") " + account_dict[menu[k]].acct_name + " " + account_dict[menu[k]].acct_number
            # prompt input from user
        print('q) uit')
        print('c) reate new account')
        user_input = raw_input('Enter choice => ')
        if user_input == 'q':
            again = 0
            print 'Bye!'
        elif user_input == 'c':
            create_account()
        else:
            user_input = int(user_input)
            print('\n')
            if menu.get(user_input) is not None:
                transaction_action = raw_input('Please enter [w] for withdrawal [d] for deposit')
                transaction_amount = input('Please enter amount')
                if transaction_action == 'd':
                    account_dict[menu[user_input]].deposit(transaction_amount)
                else:
                    account_dict[menu[user_input]].withdraw(transaction_amount)
            else:
                print('Invalid account number\n')


# Prompt user to input a account name, a unique 4 digit account number will be randomly generated
# When new account is created, a $0.0 will be deposit to the account and will be displayed in the log file
def create_account():
    # genarate new random account number
    new_ac_num = random.randint(1, 9999)
    while account_dict.get(new_ac_num) is not None:
        new_ac_num = random.randint(1, 9999)

    user_input = raw_input('Please enter account name => ')
    print('\nYour new account name is : ' + user_input)
    print('Your account number is : ' + str(new_ac_num))
    account_dict[new_ac_num] = BankAccount(str(new_ac_num), user_input)
    account_dict[new_ac_num].deposit(0)
    # create sorted menu
    index = 1
    for key in sorted(account_dict.iterkeys()):
        menu[index] = key
        index += 1


class BankAccount:
    def __init__(self, acct_number, acct_name):
        self.acct_number = acct_number
        self.acct_name = acct_name
        self.trans_lis = []
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        timestamp = time.strftime("%Y.%m.%d")
        timestamp = timestamp[2:]
        print(timestamp)
        print "You deposited", amount
        print "The new balance is :", self.balance
        output_str = '\n' + str(self.acct_number) + ':' + str(self.acct_name) + ':' + str(timestamp) + ':' + 'D' + ':' + str(amount)
        print output_str
        tempF.seek(0, 2)
        tempF.write(output_str)
        tempF.seek(0)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            timestamp = time.strftime("%Y.%m.%d")
            timestamp = timestamp[2:]
            print(timestamp)
            print "You withdrew", amount
            print "The new balance is:", self.balance
            output_str = '\n' + str(self.acct_number) + ':' + str(self.acct_name) + ':' + str(timestamp) + ':' + 'W' + ':' + str(amount)
            # write to temp file
            tempF.seek(0, 2)
            tempF.write(output_str)
            tempF.seek(0)
        else:
            print 'You can not draw more than your account balance'


if __name__ == '__main__':
    arg = 0
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    # arg = '-h'
    # read from account DB
    account_dict = {}
    menu = {}
    # read from DB
    dataFilePath = os.environ['ACCT_LIST']
    if not os.path.isfile(dataFilePath):
        dataFilePath = "dataFile.log"
        f = open(dataFilePath, "w")
        f.close()

    f = open(dataFilePath, "r+")
    # create temp file
    tempF = open("tempData.log", "w")
    tempF.seek(0)

    # Remove white line
    l = f.readline()
    while re.match(r'^\s*$', l) and l:
        l = f.readline()

    # Parsing DB to dictionary
    while l:
        tempF.write(l)
        l = l.split(':')
        if account_dict.get(l[0]) is None:
            account_dict[l[0]] = BankAccount(l[0], l[1])

        if l[3] == 'D':
            account_dict[l[0]].balance += float(l[4].strip('\n'))
            word = 'deposit'
        else:
            account_dict[l[0]].balance -= float(l[4].strip('\n'))
            word = 'withdrawal'

        account_dict[l[0]].trans_lis.append(l[2] + ' ' + word + ' ' + '$' + l[4].strip('\n'))

        l = f.readline()
    tempF.seek(0)

    # create sorted menu
    index = 1
    for key in sorted(account_dict.iterkeys()):
        menu[index] = key
        index += 1
    # create dict ac# : account for each in item
    if arg == '-i':
        account_info_menu()
    elif arg == '-h':
        account_history_menu()
    elif arg == '-t':
        account_transaction_menu()
    else:
        # Print Help
        print('Welcome to my bank')
        print('-i Account info')
        print('          User can see the account information of selected account\n\n')

        print('-h History')
        print('          User can see all transaction history of the selected account\n\n')

        print('-t Insert transaction')
        print('          User can choose or create new account to insert transaction')
        print('          To create new account input c in the transaction menu and enter account name,\n'
              '          a random 4 digit account number will be generated\n\n')

        print('          When function is running, data from the file in $ACCT_LIST will be copied to\n '
              '          \'tempData.log\',before exiting the function,\'tempData.log\' will be renamed to\n'
              '          $ACCT_LIST filename and \'tempData.log\' will be removed.\n\n ')

        print('         if function is crashed, user can recover data from the \'tempData.log\'\n'
              '         BEFORE running the function again\n\n')

        print('         if filename is not found from the environment variable:$ACCT_LIST path, a file named\n'
              '         \'dataFile.log\' will be created')
    # Close files
    f.close()
    tempF.close()

    # rename temp file to data file and remove old data file
    try:
        os.rename(dataFilePath, 'dataFile_old.log')
        os.rename('tempData.log', dataFilePath)
        os.remove('dataFile_old.log')
    except IOError:
        print 'cannot rename', arg




