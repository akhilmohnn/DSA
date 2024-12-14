"""Qn5.Prompt the user for a list of integers. For all values greater than 100,store 'over' instead , using list comprehent"""


u=input("Enter a list of integers seperated by spaces")

l=[int(x) for x in u.split()]

result=['over' if x>100 else x for x in l]

print(result)
