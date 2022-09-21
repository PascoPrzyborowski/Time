
# - saves current time and prints it
# - saves another time moment and prints it
# - prints the time that has passed in between

# import time

# start = time.time() # Startpoint Timestamp 

# gt = time.time()    # Maschine Time, General Time
# ht = time.ctime(gt) # Human Time

# print()
# print("Started on: " + ht)
# print()
# print("Time to wait ... for 5 Seconds...")
# print()
# time.sleep(1)
# print("4 Sec")
# time.sleep(1)
# print("3 Sec")
# time.sleep(1)
# print("2 Sec")
# time.sleep(1)
# print("1 Sec")
# time.sleep(1)
# print()

# gte = time.time()  # General Time, Maschine Time
# hte = time.ctime(gte) # Human Time
# print("Ended on: " + hte) # Human Time
# print()
# stop = time.time() # Stop Point Timestamp
# print()
# elapsed_time = int(stop - start) # Rounded Seconds
# print("The time of the run in Seconds exactly: ", stop - start) #Exact Maschine Time in Seconds
# print()
# print("It is rounded in full Seconds: ", elapsed_time) # Rounded Seconds
# print()

import time
import sys

str = "hello"

def print_slow(str):
    for letter in str:  #grab each letter
        sys.stdout.write(letter) # pritns out letter
        sys.stdout.flush()  #flush the line and rewrite it
        time.sleep(0.3)
        

print_slow(str)
print()
time.sleep(1)

import os

somevar = "Hello"

def print_slow2(somevar):
   for i in somevar:
        print(i)
        time.sleep(0.1)
        os.system("clear")

