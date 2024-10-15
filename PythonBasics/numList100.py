
u=input("Enter a list of integers seperated by spaces") """stored as string initially"""
numbers=u.split()
result=[]

for num in numbers:
	num1 = int(num)  """conerted into num"""
	if num1>100:
		result.append('over')
	else:
		result.append(num)
		
print("List of numbers:",result)		
			
