"""Python program to copy odd lines of one file to other"""


file=open("mits.txt","r")
l=[i for i in file]
file.close()


with open("mits2.txt", "w") as file1:
    for i in range(1,len(l)):
        if i%2!=0:
            file1.write(l[i])
   
