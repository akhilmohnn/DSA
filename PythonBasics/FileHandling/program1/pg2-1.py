"""Python program to copy odd and even lines of one file to other"""


file=open("mits.txt","r")
l=[i for i in file]
file.close()


with open("mits3.txt", "w") as file2:
    for i in range(0,len(l)):
        if i%2!=0:
            file2.write(l[i])
   
   
with open("mits4.txt", "w") as file3:
    for i in range(0,len(l)):
        if i%2==0:
            file3.write(l[i])
   
