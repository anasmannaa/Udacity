"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

"""
PSEUDO CODE

var index = 0
var max_num = 0
for i in range ((list.length) - 1):
    if i[3] > max_num:
        index = i
print result including list[index][0] as the phone number required
"""

def longest_call(re_list):
    index = 0
    max_duration = 0
    for i in range(len(re_list) - 1):
        if int(re_list[i][3]) > max_duration:
            index = i
            max_duration = int(re_list[i][3])
            
    print (re_list[index][0], "spent the longest time, ", re_list[index][3], "seconds, on the phone during September 2016.")

longest_call(calls)
