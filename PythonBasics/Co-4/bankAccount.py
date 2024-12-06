"""Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank"""

class bank:
	def __init__(self,accno,name,acctype,accblnc):
		self.accno=accno
		self.name=name
		self.acctype=acctype
		self.accblnc=accblnc
	
	def deposit(self,amount):
		if amount>0:
			self.accblnc+=amount
			print("\nSuccessfully deposited!",amount)		
		else:
			print("invalid amount!!!")
	
	def withdraw(self,amount):
		if amount>self.accblnc:
			print("insufficient balance")
		else:
			print("Succesfully withdrawn:",amount)
			self.accblnc=self.accblnc-amount
	
	def currentBalance(self):
	
		print("Your balance is: ",self.accblnc)
		
	def viewDetails(self):
		print("Account number:",accno,"\nAccount Holder: ",name,"\nAccount type: ",accblnc)			
				
					
		
accno=int(input("Enter the account number: "))
name=input("Enter the name: ")
acctype=input("Enter the account type: ")		
accblnc=int(input("Enter account balance: "))

customer1=bank(accno,name,acctype,accblnc)

while(True):
	print("<---MENU---->\n")
	print("1.Deposit\n2.WIthdraw\n3.Check balance\n4.View deatils\n5.Exit\n")
	
	ch=int(input("Enter your choice"))

	if ch==1:
		amount=int(input("Enter the amount to be deposited"))
		customer1.deposit(amount)
	elif ch==2:
		amount=int(input("Enter the amount to be withdrawn"))
		customer1.withdraw(amount)
	elif ch==3:
		customer1.currentBalance()
	elif ch==4:
		customer1.viewDetails()
	elif ch==5:
		break
	else:
		print("Invalid choice")				
		
		
