  	   
n = int(input("Enter the current year: "))
year = int(input("Enter the year to search: "))

for i in range(n, year + 1):
    if (i % 400 == 0) or (i % 100 != 0 and i % 4 == 0):
        print(i,"is a leap year.")
    else:
        print(i," is not a leap year.")
