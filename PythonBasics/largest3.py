"""DATE:03/10/24
2.To read three numbers and print largest among them
"""

#PROGRAM:
x=int(input("Enter first number"))
y=int(input("Enter second number"))
z=int(input("Enter second number"))

if x>y and x>z:
	print("First number is larger")
elif y>x and y>z:
	print("Second number is largest")
else:
	print("Third is largest")		
	
	
"""OUTPUT: Enter first number3
	      Enter second number4
		 Enter second number6
		 Third is largest  ""

