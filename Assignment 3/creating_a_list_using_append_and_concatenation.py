def list_of_items():
    items = []

    # Add the first four items to the list called items using append. (one per item).
    items.append(67)
    items.append(62.9)
    items.append("hi")
    items.append(False)

    # Add the last four items to the list called items using concatinate.
    items += [8]
    items += [67]
    items += ['apple']
    items += [6.5]

    return items

# Function call to list_of_items function then display the return list of items.
print(list_of_items(), end='')  # The end='' is used to specify that there is no newline.