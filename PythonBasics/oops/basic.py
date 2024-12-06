"""
Qn1. create a class student with attributes number,name and age :
	1.1 create an object student1 of the student class
	1.2 print the roll no ,name and age """
	
class Student:
	
	def __init__(self,rollno,name,age):
		self.rollno=rollno
		self.name=name
		self.age=age
		

rollno=int(input())
name=input()
age=int(input())		
student1=Student(rollno,name,age)

print("Roll no student1: ",student1.rollno)		
print("Name student1: ",student1.name)		
print("Age student1: ",student1.age)		

			
	
