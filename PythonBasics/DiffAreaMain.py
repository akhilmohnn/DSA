from Graphics import rectangle,circle
from Graphics.threeD import cuboid,sphere

"""Rectangle module"""
length=int(input("Enter rectangle length: "))
width=int(input("Enter rectangle width: "))
print("Area of rectangle: ",rectangle.Area(length,width))
print("Perimeter of rectangle: ",rectangle.Perimeter(length,width))


"""Circle module"""
r=float(input("Enter the radius: "))
print("Area of circle is: ",circle.circArea(r))
print("Perimeter of circle: ",circle.circPerimeter(r))


"""Cuboid module"""
length=int(input("Enter rectangle length: "))
width=int(input("Enter rectangle width: "))
height=int(input("Enter rectangle height: "))
print("Area of cuboid is: ",cuboid.surfaceArea(length,width,height))
print("Volume of cuboid is: ",cuboid.volume(length,width,height))



