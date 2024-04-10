"""
3.	Here is a dictionary of the days in the months of the year: 
•	days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31} 
a)	Ask the user to enter a month name and use the dictionary to tell them how many days are in the month. 
b)	Print out all of the keys in alphabetical order. 
c)	Print out all of the months with 31 days. 
d)	Print out the (key-value) pairs sorted by the number of days in each month

"""
days = {
    'January':31, 'February':28,
    'March':31, 'April':30,
    'May':31, 'June':30,
    'July':31, 'August':31,
    'September':30, 'October':31,
    'November':30, 'December':31
}

# Print all the month's name
print("─" * 100 + "\n" + "MONTH'S NAME".center(100) + "\n" + "─" * 100)
for key in days:
    if key != 'December':
        print(key, end=', ')
    else:
        print(key)
print("─" * 100)
"""
Alternative solution to print all the month's name
print(days.keys())
"""

month = input("Enter a month name: ").title()   # Ask user to input a month name then convert every first letter of the word into uppercase.
while month not in days:    # Loop as long as the user's inputted for the month is not in the dictionary.
    print(f"\n'{month}' is not in the dictionary! Please enter valid month!")
    month = input("Enter a month name: ").title() # Ask user to input a month name then convert every first letter of the word into uppercase.
print(f"There are {days[month]} days in a month of {month}!\n")   # Tell user how many days are in the month.
print(f"Keys in alphabetical order:\n{sorted(days)}\n") # Sort the keys in alphabetical order then print all the keys.

print("MONTHS THAT HAS 31 DAYS:")
for key in days:
    if days[key] == 31:
        print(key)

# Sort all items in the days dict according to the days in months.
sorted_dict = dict(sorted(days.items(), key=lambda x: x[1]))
print("\nMONTHS THAT ARE SORTED BY NUMBER OF DAYS:")
for key in sorted_dict:
    print(f"{key}: {sorted_dict[key]}")