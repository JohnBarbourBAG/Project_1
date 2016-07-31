from datetime import datetime as dt
import pymysql
from random import uniform as U


#the current time the script runs
#turn the time into a string
blastoff_string = dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S %z")

print("blastoff.py occured at: {}".format(blastoff_string))



#stuff the string into the database
print("INSERT {} INTO Table".format(blastoff_string))



#create the next blastoff time randomly
yr = int(dt.utcnow().strftime("%Y"))
mo = int(dt.utcnow().strftime("%m"))
da = int(dt.utcnow().strftime("%d"))
hr = int(24*U(0,1))
min = int(60*U(0,1))
sec = int(60*U(0,1))

print("{}-{}-{}".format(yr, mo, da))

next_blastofftime = dt(year=yr, month=mo, day=da, hour=1)
print('change')

#write the next blastoff time to the textfile

#uses common log format for time [10/oct/2009:13:55:36 -0700]


#one change

#
# the datetime.strptime() class method creates a datetime object from a string representing a date and time and a corresponding format string. datetime.strptime(date_string, format)
#
#
