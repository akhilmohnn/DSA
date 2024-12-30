"""Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
find sum of 2 time"""

class time:
    
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
        
    def sum(self,other):
        tot_sec = self.second + other.second
        tot_min = self.minute + other.minute + tot_sec // 60
        tot_hr = self.hour + other.hour + tot_min // 60
        tot_sec %= 60
        tot_min %= 60
        return time(tot_hr,tot_min,tot_sec)
    
    def __add__(self,other):
        return self.sum(other) 
    
print("Time1")
hour=int(input("enter the hour"))
minute=int(input("enter the minute"))
second=int(input("enter the second"))
time1=time(hour,minute,second)

print("Time2")
hour=int(input("enter the hour"))
minute=int(input("enter the minute"))
second=int(input("enter the second")) 
time2=time(hour,minute,second)
t3=time1+time2
print("sum of time:"+str(t3.hour)+":"+str(t3.minute)+":"+str(t3.second))
