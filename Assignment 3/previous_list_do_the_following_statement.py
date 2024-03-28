from creating_a_list_using_append_and_concatenation import list_of_items    # This allow us to access the file of creating_a_list_using_append_and_concatenation.

print(" <-- Unchanged list")
items = list_of_items() # Function call to list_of_items then assign the return list to items variable.

# a. Append “banana” and 67 to the list.
items.append("banana")
items.append(67)
print(f"After appending 'banana' and 67: {items}")

# b. Insert the value "dog" at position 3.
items.insert(3, "dog")
print(f"After inserting the 'dog' at position 3: {items}")

# c. Insert the value 909 at the start of the list.
items.insert(0, 909)
print(f"After inserting 909 at the start of the list: {items}")

# d. Find the index of “hi”.
print("Index of 'hi':", + items.index("hi"))

# e. Count the number of 67s in the list.
print(f"Occurrences of 67: {items.count(67)}")

# f. Remove the first occurrence of 67 from the list.
items.remove(67)
print(f"After removal of the first occurrence of 67: {items}")

# g. Remove False from the list using pop and index
items.pop(4)
print(f"After removal of False using pop and index: {items}")