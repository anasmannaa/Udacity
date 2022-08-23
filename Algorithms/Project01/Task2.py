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
    calls_map = {}
    for call in re_list:
        caller = call[0]
        reciever = call[1]
        duration = int(call[3])
        if caller in calls_map:
            calls_map[caller] += duration
        else:
            calls_map[caller] = duration

        if reciever in calls_map:
            calls_map[reciever] += duration
        else:
            calls_map[reciever] = duration

    longest_duration = 0
    phone_number = ""
    for key in calls_map:
        if calls_map[key] > longest_duration:
            longest_duration = calls_map[key]
            phone_number = key
    print (phone_number, "spent the longest time, ", longest_duration, "seconds, on the phone during September 2016.")
        
longest_call(calls)
