l=input("Enter the list of integers seperated by spaces:")
l1=[int(num) for num in l.split()]
print(l1)
pl=[num for num in l1 if num>0]

print("\n","positive are:",pl)

sq=[i*i for i in pl if i>0]
print("Squares are:",sq)

ng=input("Enter negative numbers with spaces")
ng1=[int(i) for i in ng.split()]
ng2=[i for i in l1 if num<0]
