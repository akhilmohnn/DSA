f=open("textfile2.txt","w")

f.write("File content removed")

f.close()

f=open("textfile2.txt","r")

print(f.read())
