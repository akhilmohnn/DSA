f=open("textfile.txt","a")

f.write("Additional line added by writing")
f.close()

"""After writing --> Now to print"""

f=open("textfile.txt","r")
print(f.read())
