"""Write lambda function to find area of square, rectangle and triangle"""

areaOne=lambda a:a*a
areaTwo=lambda l,b:l*b
areaThree=lambda b,h:.5*b*h

s=int(input("Enter the side of the square:"))
print("Area of the square:",areaOne(s))

p=int(input("Enter the length of rectangle:"))
q=int(input("Enter the length of rectangle:"))
print("Area of the square:",areaTwo(p,q))


p=int(input("Enter the breadth of triangle:"))
q=int(input("Enter the height of triangle:"))
print("Area of the square:",areaThree(p,q))
