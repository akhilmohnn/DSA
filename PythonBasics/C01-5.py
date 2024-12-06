"""Qn5.Prompt the user for a list of integers. For all values greater than 100,store 'over' instead """

u=input("Enter a list of integers seperated by spaces")
numbers=u.split()
result=[]

for num in numbers:
	num1 = int(num)
	if num1>100:
		result.append('over')
	else:
		result.append(num)
		
print("List of numbers:",result)		
			
