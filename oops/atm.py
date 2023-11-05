class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        user_input = input('''
            Hello, how would you like to proceed?
            1. Create pin
            2. Deposit money
            3. Withdraw money
            4. Check balance
            5. Exit
        ''')
        if user_input == '1':
            self.create_pin()
        elif user_input =='2':
            self.deposit_money()
        elif user_input =='3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print('bye')

    def create_pin(self):
        pin = input("Enter your pin")
        self.pin = pin
        print("Pin set successfully")
    
    def deposit_money(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount to be deposited "))
            self.balance += amount
            print("Deposit successful")
        else:
            print("Invalid pin")
    
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount to be withdrawn "))
            if amount <= self.balance:
                self.balance-=amount
                print("Operation successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")
    
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")