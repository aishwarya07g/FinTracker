from model import *
from datetime import datetime


db.connect()
def signup():
	username = input("Create Username: ")
	password = input("Create Password: ")

	exists = len(User.select().where(User.username == username))

	if not exists:
		User.create(username=username, password=password)
		print("User created Successfully!\n\n")

	else:
		print("Username already exists. Please try new username.")


def login():
	username = input("Enter username: ")
	password = input("Enter password: ")

	user = User.select().where(User.username ==username)

	if len(user):
		if User.password==password:
			print("Login Successfull! \n")
			return user.get()

		else:
			print("Invalid Password.\n\n")

	else:
		return None


def create_wallet(user):
	name = input("Enter Wallet Name: ")
	bal = input("Enter Starting Balance: ")
	wallet = Wallet.create(name=name, balance=bal, owner=user, last_transaction=datetime.now())
	print("\nWallet Created Successfully..\nCurrent Balance: 0")

def check_balance(user):
	wallets = user.wallets

	for wallet in wallets:
		print(wallet.id, wallet.name, wallet.balance)


def add_transaction(user):
	wallets = user.wallets

	for wallet in wallets:
		print(wallet.id, wallet.name, wallet.balance)

	ch = int(input("\nChoose a Wallet ID: "))

	wallet = Wallet.get(Wallet.id == ch)
	is_expense = int(input("\nChoose Type:\n0. Income\n1. Expense\n-->"))

	if not is_expense:
		from_person = input("From Who: ")
	else:
		from_person = "None"

	trans_name = input("Enter Purpose: ")
	amount = float(input("Enter Amount: "))
	comment = input("Any comments? \n")

	Transaction.create(owner=user,
		wallet=wallet,
		name=trans_name,
		amount=amount,
		from_person=from_person,
		timestamp=datetime.now(),
		comment=comment,
		is_expense=bool(is_expense))

	if not is_expense:
		wallet.balance += amount
	else:
		if amount > wallet.balance:
			print("--! Balance not Sufficient. Please Add Money before you Borrow. !--")
		else: 
			wallet.balance -= amount
	
	wallet.save()




def see_transaction(user):
	trans = user.expenses

	for txn in trans:
		if txn.is_expense:
			print(txn.wallet, txn.name, f"-{txn.amount}", txn.timestamp)
		else:
			print(txn.wallet, txn.name, f"+{txn.amount}", txn.timestamp)



