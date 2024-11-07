"""Q1.Create a list with values 3,56,12,98,43,23 write a program to find the largest number in the given list of numbers, 
1.1. find the sum of all elements in the list 
1.2 find all even numbers from the given list
1.2 for all value greater than 50 store the word "over"

1.4 find the smallest element in the list ,reverse the list 
1.5 add the elements 500 to the list
1.6 sort the list
"""

numbers = [3,56,12,98,43,23]
print("Initial number of list:",numbers)

largest=max(numbers)
print("\nLargest of list:",largest)

print("\nSum of all elements in the list:",sum(numbers))

numEven = [i for i in numbers if i%2==0]
print("\nEven numbers are:",numEven)

greater56 = ["over" if i>50 else i for i in numbers]
print("\nPrinting with over:",greater56)

smallest=min(numbers)
print("\nSmallest number:",smallest)

numbers.reverse()
print("Reverse order:",numbers) 

numbers.append(500)
print("\nLatest list:",numbers)

new=int(input("\nEnter a number to add:"))
numbers.append(new)
print("list after entering the",new,":",numbers)

numbers.sort()
print("\nOrdered in sort:",numbers)
