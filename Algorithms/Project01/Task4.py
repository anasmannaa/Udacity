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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def probability_test(list1, list2):
    prob_nums = []
    calls_from = []
    calls_to = []
    texts_from = []
    texts_to = []
    for call in list1:
        calls_from.append(call[0])
        calls_to.append(call[1])
    for text in list2:
        texts_from.append(call[0])
        texts_to.append(call[1])

    for i in calls_from:
        if i not in prob_nums:
            if i not in calls_to:
                if i not in texts_from and i not in texts_to:
                    prob_nums.append(i)
    prob_nums.sort()
    print("These numbers could be telemarketers: ")
    for i in prob_nums:
        print(i)

probability_test(calls, texts)
