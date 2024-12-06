class Rectangle:
	
	def __init__(self,length,breadth):
		
		self.length=length
		self.breadth=breadth
	
	def area(self):
		return self.length*self.breadth
		
	def perimeter(self):
		return 2*(self.length+self.breadth)	

     
length1=int(input("Length of first rectangle: "))
breadth1=int(input("Breadth of first rectangle: "))	

length2=int(input("Length of second rectangle: "))
breadth2=int(input("Breadth of second rectangle: "))

rectangle1=Rectangle(length1,breadth1)	
rectangle2=Rectangle(length2,breadth2)	

area1=rectangle1.area()
perimeter1=rectangle1.perimeter()

area2=rectangle2.area()
perimeter2=rectangle2.perimeter()
		
if(area1>area2):
	print("Area of first rectangle is larger","(",area1,")")
elif(area2>area1):
	print("Area of second rectangle is larger","(",area2,")")
else:
	print("Both are equal")		
	
