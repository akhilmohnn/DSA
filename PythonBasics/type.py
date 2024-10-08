"""DATE:03/10/24
2.To read numbers,string and printing the type
"""

#PROGRAM:
a=int(input("Enter first number"))

b=int(input("Enter second number"))

c=input("Enter a string")
print("Strig is:",c)

print("Numbers are:",a,"and",b)
print("Sum is:",a+b)

print(type(c))
print(type(a))


sum=a+b

if sum>5:
  print("Sum is grater than 5")
else:
  print("Less than 5") 
  
"""OUTPUT: Enter first number2
Enter second number3
Enter a stringstr
Strig is: str
Numbers are: 2 and 3
Sum is: 5
<class 'str'>
<class 'int'>
Less than 5
"""
