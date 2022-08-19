"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
PSEUDO CODE
create newArray
for all numbers in records:
    if number ! in new array:
        add number
    
return newArray length
"""

def count_identities(list1, list2):
    identical_numbers = []
    for num in list1:
        if num[0] not in identical_numbers:
            identical_numbers.append(num[0])
        if num[1] not in identical_numbers:
            identical_numbers.append(num[1])
    for num in list2:
        if num[0] not in identical_numbers:
            identical_numbers.append(num[0])
        if num[1] not in identical_numbers:
            identical_numbers.append(num[1])
    return len(identical_numbers)

print("There are ", count_identities(texts, calls), "different telephone numbers in the records.")
