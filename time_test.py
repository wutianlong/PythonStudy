import time

print(" time.ctime() =  %s " % time.ctime())

time.sleep(5)

print("time.ctime() = %s " % time.ctime())



print("formate time = %s" % time.strftime( "%Y-%m-%d %H:%M:%S",  time.localtime()) )
