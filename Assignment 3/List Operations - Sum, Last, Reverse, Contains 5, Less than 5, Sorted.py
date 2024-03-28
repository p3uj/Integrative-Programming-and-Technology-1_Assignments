listOfInt = []
sizeOfList = int(input("Enter the size of list: "))
lessThan5 = 0

while True:
    try:
        while len(listOfInt) != sizeOfList:
            listOfInt.append(int(input("Enter an integer: ")))
        break
    except ValueError:
        print("\nInvalid input! Input must be an integer only!")
print(f"Sum of items: {sum(listOfInt)}")
print(f"Last item in the list: {listOfInt[-1]}")
listOfInt.reverse() # Reversing the items in the list using reverse method.
print(f"Reverse order: {listOfInt}")

# Printing if list contains a 5.
if 5 in listOfInt:
    print("Yes")
else:
    print("No")

# Printing the occurrences of less than 5 in the list.
for item in listOfInt:
    if item < 5:
        lessThan5 += 1
print(f"Occurrences of less than 5: {lessThan5}")

# Removing the first and last items from the list.
listOfInt.pop(0) # Remove the first item.
listOfInt.pop() # Remove the last item

listOfInt.sort()
print(f"Sorted items: {listOfInt}")