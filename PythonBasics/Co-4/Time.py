"""Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
find sum of 2 time"""

class Time:
	def __init__(self,hour,minute,second):
		self.hour=hour
		self.minute=minute
		self.second=second
		
	def __add__(self,other):
		
		
hour=int(input("Enter the hours : "))
minute=int(input("Enter the minutes: "))
seconds=int(input("Enter the seconds: "))				
