"""DATE:04/10/24
2.Display future leap years from current year to a final year entered by user."""

#PROGRAM
  	   
n = int(input("Enter the current year: "))
year = int(input("Enter the year to search: "))

for i in range(n, year + 1):
    if (i % 400 == 0) or (i % 100 != 0 and i % 4 == 0):
        print(i,"is a leap year.")
    else:
        print(i," is not a leap year.")
  	   
  	 
"""OUTPUT:Enter the current year: 2024
Enter the year to search: 2030
2024 is a leap year.
2025  is not a leap year.
2026  is not a leap year.
2027  is not a leap year.
2028 is a leap year.
2029  is not a leap year.
2030  is not a leap year.
 """  	   
  	   
