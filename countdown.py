# - takes an  int as input
# - uses this int as a countdown
# - visibly counts down
# - prints begin time, end time and countdown int

import time

start = time.time() # Startpoint Timestamp 

gt = time.time()    # Maschine Time, General Time
ht = time.ctime(gt) # Human Time

print()
print("Started on: " + ht) #print Timestamp
print()
tdf = input("Time Delay Factor to Countdown: ") #input of the Countdown Factor 
tdf1 = int(tdf) # Variable in int convert because input is always string
print()
print("Your Time Delay Faktor is:" +" "+ tdf + " Seconds !") #print what your number is
print()
print("Time to wait ... for " +tdf + " Seconds...for Detonation!") # something to print
print()
while tdf1 != 0:  #While as long not 0
    tdf1 = tdf1-1 # count -1 of the variable
    time.sleep(1) #some delay
    print(tdf1)     #print the current variable with  each - 1
    time.sleep(1)   #some delay
    if tdf1 == 0:   # if countdown is 0 print something
        print()
        print("See You...Detonation...imminent! ") # print Countdown successfull
        print()

gte = time.time()  # General Time, Maschine Time
hte = time.ctime(gte) # Human Time
print("Ended on: " + hte) # Human Time
print()
stop = time.time() # Stop Point Timestamp
print()
elapsed_time = int(stop - start) # Rounded Seconds
print("The time of the run in Seconds exactly: ", stop - start) #Exact Maschine Time in Seconds
print()
print("It is rounded in full Seconds: ", elapsed_time) # Rounded Seconds
print()

