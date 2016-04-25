import threading
import time
import random

b = 0
def hello(i):
    print threading.current_thread().name
    global b
    b += 1
    c = random.random()
    c += 1
    print "Before Slepp: \nThis is thread " + str(i) + '. \n', "This is " + str(b) + '. \n', "This is a random number: " + str(c) + '. \n'
    #print threading.enumerate()
    print threading.current_thread()
    i += 1
    time.sleep(1) 
    print "After Sleep: \nThis is thread " + str(i) + '. \n', "This is " + str(b) + '. \n', "This is a random number: " + str(c) + '. \n'
    

for i in range(10):
    print i
    threading.active_count()
    a = threading.Thread(target=hello, args=(i, ))
    a.start()
print 'Bingo! '