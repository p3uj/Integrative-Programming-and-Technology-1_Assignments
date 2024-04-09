"""
Instruction: 1.	Write a Python program to create a list of tuples having first element as the number and second element 
as the square of the number. Input: list = [1, 2, 3] Output: ((1, 1), (2, 4), (3, 9)).
"""
input_list = [1, 2, 3]  # Initial element of the list.

for item in input_list: # Loop through each of the elements.
    input_list[input_list.index(item)] = (item, item*item)  # Update the element.

# Convert the input_list into tuple to create tuple with the elements of number and its square of that number.
tuple_elements = tuple(input_list)
print(tuple_elements)