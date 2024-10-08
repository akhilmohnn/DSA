year=int(input("Enter the year to search"))
if ((year%400==0) or (year%100!=0) and (year%4==0)):
        print("It is a leap year");
else:
  	   print("Not a leap year");	
