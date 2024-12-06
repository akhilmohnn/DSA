import re

animal="Huge wild tusker"
a1=re.search("^Huge.*tusker$",animal)


if a1:
	print("Yes true")
else:
	print("No match")	


x="Hello\nworld"
print(x)

Raw=r"Hello\nWorld"
print(Raw)
