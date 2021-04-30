
import time
from datetime import datetime
delay = (float(input("GIve a time delay \n")))

while True:
 now = datetime.now()
 current_time = now.strftime("%H:%M:%S")
 
 print("the time is: " + str(current_time))
 
 time.sleep(delay)
