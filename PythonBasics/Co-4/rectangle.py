"""Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to
													compare the area of 2 rectangles."""
													
													
class Rectangle:
	def __init__(self,length,width):
		self.length=length
		self.width=width
		
	def area(self):
		return self.length*self.width	
							
	def __lt__(self,other):
		return self.area() < other.area()
	
length=int(input("Enter the length1: "))
width=int(input("Enter the width1: "))

rec1=Rectangle(length,width)


length=int(input("Enter the length2: "))
width=int(input("Enter the width2: "))

rec2=Rectangle(length,width)

if rec1 < rec2 :
	print("Area of rectangle1 is smaller than area of rectangle2")
elif rec1 > rec2 :
	print("Area of rectangle1 is larger than area of rectangle2")
else:
	print("Both rectangles have same area")
		
