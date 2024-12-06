"""Create two lists of colors list with colors red,blue,green,yellow,purple and list2 with colors blue,yellow,pink use a set to find colors in list1 that are not in list2"""


list1=["red","blue","green","yellow","purple"]
list2=["blue","yellow","pink"]

result=set(list1)-set(list2)
print(result)

print("As list: ",list(result))
