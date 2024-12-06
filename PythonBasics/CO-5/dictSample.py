import csv

Sdict=[
	{'branch':'MCA','name':'Akhil','Mark':70},
	{'branch':'MTC','name':'Akarsh','Mark':80},
	{'branch':'TYU','name':'Alan','Mark':90}
		]
	
field=['name','branch','Mark']

filename="university.csv"

with open('filename','w') as file1:
	write=csv.DictWriter(file1,filename=field)
	
	writer.writeheader()
	
	writer.writerows()		
