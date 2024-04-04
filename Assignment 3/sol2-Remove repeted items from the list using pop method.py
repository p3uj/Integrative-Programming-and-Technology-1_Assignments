elements_list = [1, 1, 2, 3, 4, 3, 0, 0]    # Initial elements of the list.
for i in elements_list: # Loop until it reach the last elements in the list.
    if elements_list.count(i) > 1:  # Check and execute if the occurrences of the element is more than 1.
        second_index = elements_list.index(i, elements_list.index(i) + 1)   # Find the second index of the element.
        elements_list.pop(second_index) # Remove the element in the second index using pop method.
print(elements_list)    # Print the updated elements in the list.