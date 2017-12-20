import time

#EPOCH is the time of January 1 1970 00:00:00
#time() produces a string that denotes the second passed after EPOCH
print("Seconds passed after EPOCH: "+str(time.time()))
#gmtime() produces a time structure that denotes the current time with format such as
#tm_year:year of the particular day,tm_month:month of the particular day
#tm_date:date of the day,tm_day:day of the week
#tm_min:minutes,tm_hour:hours,tm_seconds:seconds
#tm_yday : denotes number of days passed in the calender year
tim=time.gmtime()
print("Current time using gmtime()"+str(tim))
#ctime() convert time to 24 character string
#Seconds can be passed as parameter to ctime() function
print("Time using ctime():"+time.ctime())
#asctime() converts gmtime() time structure to 24 character string
#takes input as gmtime() time structure object
print("Time using asctime():"+time.asctime(tim))

#using sleep
#used to introduce delay(switching execution or control) by a specific number of miliseconds in the program
#take parameter the delay to be introduce
time.sleep(4)
print("Time after sleep:"+time.ctime())
