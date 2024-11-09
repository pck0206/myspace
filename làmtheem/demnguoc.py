import time
x = int(input())
for i in reversed(range(0,x)):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = i // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME OUT !")