"""Create a class Publisher (name). Derive class Book from Publisher with attributes title and
author. Derive class Python from Book with attributes price and no_of_pages. Write
a
program that displays information about a Python book. Use base class constructor invocation and
method overriding."""

class Publisher:
	def __init__(self,name):
		self.name=name
	
	def display():
		pass	
	

class Book(Publisher):
	def __init__(self,name,title,author):
		super().__init__(name) #invoking the base class publisher
		self.title=title
		self.author=author
		
	def display():
		pass	
		


class Python(Book):
	def __init__(self,name,title,author,price,pageno):
		super().__init__(name,title,author)
		self.price=price
		self.pageno=pageno
		
	def display(self):
		print("\nBook Details:\nPublisher: ",self.name,"\nTitle: ",self.title,
		      "\nAuthor: ",self.author,"\nPrice: ",self.price,"\nPageno:",self.pageno) 
			
			
	
name=input("Enter the publisher's name:")
author=input("Enter author name: ")
title=input("\nEnter the title of the book:")
price=int(input("Enter the price: "))
pageno=int(input("\nEnter the number of pages:"))	


book1=Python(name,title,author,price,pageno)
book1.display()
