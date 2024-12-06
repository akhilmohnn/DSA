import csv

data=[
	[200,"AnakSunamun",23,"QN"],
	[400,"Imhotep",23,"KG"],
	[600,"Valak",23,"RULER"]
	]
	
with open("student.csv",mode="w",newline="") as file:
	csvWrite=csv.writer(file)
	csvWrite.writerows(data)
	

print("Additional data written to csv");		
