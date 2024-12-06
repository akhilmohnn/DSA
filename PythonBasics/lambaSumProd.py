"""Write lambda function to find sum of 3 three nmbrs,product of three numbers"""

Sum=lambda a,b,c:a+b+c

Prod=lambda a,b,c:a*b*c

num1, num2, num3 = map(int, input("Enter three integers separated by spaces:").split())

print("Sum of three numbers:",Sum(num1,num2,num3))
print("Product of three numbers:",Prod(num1,num2,num3))
