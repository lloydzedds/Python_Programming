print("Welcome to day 15")
print("We have an exercise, The exercise is to print good morning or good evening based upon the time")
print("we are importinf the timpstamp module to build this code")

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamph = int(time.strftime('%H'))
print(timestamp)
timestampm = int(time.strftime('%M'))
print(timestamp)
timestamps = int(time.strftime('%S'))
print(timestamp)
if (timestamph >= 19):
    print("Good Night sir")
elif(timestamph >= 14):
    print("Good Evening sir")
elif(timestamph >= 11):
    print("Good Afternoon sir")
elif(timestamph >= 5):
    print("Good Morning sir")