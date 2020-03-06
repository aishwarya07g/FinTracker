from app import *

while True:
	print("-"*30)
	print("Welcome to FinTracker", "-"*30, sep="\n")

	print("What would you like to do today? \n\
		1. Login \n\
		2. Signup \n\
		3. Exit")

	choice = input("Enter Choice: ")

	if choice == "1":
		user = login()

		while user is not None:
			print("Choose Operations:\n\
		1. Create Wallet\n\
		2. Add Transaction\n\
		3. Check Balance\n\
		4. See Transaction")

			ch = input("\n--> ")

			if ch == "1":
				create_wallet(user)
			elif ch == "2":
				add_transaction(user)
			elif ch == "3":
				check_balance(user)
			elif ch == "4":
				see_transaction(user)
			else:
				break

		else:
			print("Credentials do not match. or Create a New Account.\n")




	elif choice == "2":
		signup()

	else: 
		break