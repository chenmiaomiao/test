import threading
import time
from ensurepip import __main__

def a():
    print 'a_begin'
    time.sleep(3)
    print 'a_end'
    
def b():
    print 'b_begin'
    time.sleep(1)
    print 'b_end'
    
    
if __name__ == '__main__':
    a_t = threading.Thread(target=a)
    b_t = threading.Thread(target=b)
    
    threads = []
    threads.append(a_t)
    threads.append(b_t)
    
    for thread in threads:
        thread.start()
    #===========================================================================
    # a_t.start()
    # a_t.join()
    # 
    # b_t.start()
    # b_t.join()
    #===========================================================================
    
    for thread in threads:
        thread.join()
    
    print 'bingo'
    