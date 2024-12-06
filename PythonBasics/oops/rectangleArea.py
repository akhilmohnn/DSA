class Rectangle:
	
	def __init__(self,length,breadth):
		
		self.length=length
		self.breadth=breadth
	
	def area(self):
		return self.length*self.breadth
		
	def perimeter(self):
		return 2*(self.length+self.breadth)	
		
		

length=int(input())
breadth=int(input())	

rectangle=Rectangle(length,breadth)	

area=rectangle.area()
perimeter=rectangle.perimeter()

		
print("Area of rectangle is:",area)

print("Perimeter of rectangle is:",perimeter)		
