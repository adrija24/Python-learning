import time
# time.time()
print(time.time())
def usingfor():
    for i in range(50000):
        print(i)

init = time.time()
usingfor()
print(time.time() - init)

# time.sleep()
print("Hiiii")
time.sleep(5)
print("This is printed after 5 seconds")

# time.strftime()
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("Current time:", formatted_time)