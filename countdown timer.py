import time
def countdown(t):
    while t>0:
        print(t)
        t = t-1
        time.sleep(1)
    print("Time's Up")

print("How many seconds to count down? Enter an Integer.")
seconds = input()
while not seconds.isdigit():
    print("that wasn't an integer number! Please Enter an Integer")
    seconds = input()
seconds = int(seconds)
countdown(seconds)
