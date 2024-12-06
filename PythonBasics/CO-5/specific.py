import csv

specific=int(input("Enter the row to search: "))

with open("student.csv",mode="r") as file:
	rows=list(csv.reader(file))
	
	
	if specific<len(rows):
		print(f"Row {specific} -> {rows[specific]}")
	else:
		print(f"Row{specific} Does not exist")	
