import time

t = time.localtime()
current_time = time.strftime("%H:%M", t)
print(current_time)
if current_time < "12:00":
    print("Good morning\n")
elif current_time == "12:00":
    print("Good noon\n")
elif current_time >="12:01" and current_time <= "16:00":
    print("Good afternoon\n")
elif current_time >= "16:01" and current_time <= "20:00":
    print("Good evening\n")
elif current_time >= "20:00" and current_time <= "23:59":
    print("Good night\n")