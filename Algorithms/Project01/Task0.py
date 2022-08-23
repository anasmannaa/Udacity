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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def printFirstText(list):
    print ('First record of texts,', list[0], ' texts ', list[1], ' at time ', list[2])  
    
def printLastCall(list):
    print ('Last record of calls,', list[0], ' calls ', list[1], ' at time', list[2], ' lasting ', list[3], 'seconds')


printFirstText(texts[0])
printLastCall(calls[-1])
