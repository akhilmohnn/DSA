n=int(input("Enter the number of colors to insert:"))

color1=[]
print("Enter the colors for list1")
for x in range(n):
    color=input()
    color1.append(color)

color2=[]
print("Enter the colors for list2")
for x in range(n):
    color=input()
    color2.append(color)

unique=[]
for x in color1:
    if x not in color2:
        unique.append(x)

print("Unique colors are: ",unique)