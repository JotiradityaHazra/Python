import time 
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

print(timestamp)

# your program should greet you Good morning, good afternoon, or good evening based on the current time

time=int(time.strftime("%H")) 

print(time)

if time <12 :
    print("Good Morning")
elif time <= 17:
    print("Good Afternoon")
else:
    print("Good Evening")   