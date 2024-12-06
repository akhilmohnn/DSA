"""Write a Python program to read a file line by line and store it into a list."""

file=open("mits.txt","r")
l=[i.split() for i in open("mits.txt")]
file.close()


