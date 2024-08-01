'''
3. Simulate Stopwatch Program
a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
b. I/P -> Start the Stopwatch and End the Stopwatch
c. Logic -> Measure the elapsed time between start and end
d. O/P -> Print the elapsed time
'''

import time

def stopwatch():
    input("press enter to start the stopwatch")
    start_time=time.time()
    print(f"the start time is {start_time}")

    input("press enter to stop the watch ")
    end_time=time.time()

    print(f"the end time is {end_time}")

    elapased_time=end_time-start_time

    return elapased_time

print(stopwatch())

