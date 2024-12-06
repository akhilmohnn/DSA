"""Print out all colors from color-list1 not contained in color-list2."""
"""Create color list given as user inputs , use list comprhent""" 

list1=[i for i in input("Enter the colors in list 1:").split()]

list2=[i for i in input("Enter the colors in list 2:").split()]


result=[i for i in list1 if i not in list2]
print("Colors in list1 is:",result) 

