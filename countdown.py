import time


def countdown(time_sec):
    while time_sec:
        mins, sec = divmod(time_sec, 60)
        time_format= f'0{mins}:0{sec}'
        print(time_format)
        time.sleep(1)
        time_sec = time_sec - 1




time_lapse = int(input("enter time for starting countdown:"))


countdown(time_lapse)
print("time is up!!!!")
