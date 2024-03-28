def remove_duplicates_elements(list_elements):
    unique_elements = list(dict.fromkeys(list_elements))    # Create a new dictionary with keys of list_elements then convert it to list. The dictionary will automatically removed duplicates elements.
    return unique_elements  # Return the removed duplicates elements from the list to the calling function

original_list = [1, 1, 2, 3, 4, 3, 0, 0]
# Function call to remove_duplicates_elements function with parameter of original_list. Then display the return list.
print(f"The list after removing duplicates elements: {remove_duplicates_elements(original_list)}")