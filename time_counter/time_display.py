import time
my_time=int(input("Enter the time in seconds: "))

for i in range(my_time,0,-1):
    second=i%60
    minutes=int(i/60)%60
    hour=int(i/3600)%24
    print(f"{hour:02},{minutes:02},{second:02}")
    time.sleep(1)
print("Time's Up!")