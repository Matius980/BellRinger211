import time
Period5hour = 14
Period5minute = 19

while True:
    currenttime = time.localtime()
    currenthour = currenttime.tm_hour
    currentminute = currenttime.tm_min
    remaininghours = Period5hour - currenthour
    remainingminutes = Period5minute - currentminute
    if remainingminutes < 0:
        remaininghours -= 1
        remainingminutes += 60
    print(f"Time remaining until class ends: {remaininghours} hours and {remainingminutes} minutes.")
