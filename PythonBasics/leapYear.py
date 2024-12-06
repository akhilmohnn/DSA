"""DATE:03/10/24
2.To read an year and print whether it is leap or not"""

#PROGRAM

year=int(input("Enter the year to search"))
if ((year%400==0) or (year%100!=0) and (year%4==0)):
        print("It is a leap year");
else:
  	   print("Not a leap year");	

"""OUTPUT:Enter the year to search2024
          It is a leap year


          Enter the year to search2028
          It is a leap year
 """
