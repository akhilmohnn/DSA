"""To print triangle star pattern"""

n = int(input("Enter the size: "))

# Loop through each row for the original triangle
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# Loop through each row for the inverted mirror triangle
for i in range(n):
    for j in range(n-i-1):
        print("*", end=" ")
    print()
