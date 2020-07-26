import time
import threading

def test():
    print(time.ctime())
    threading.Timer(60,test).start()

test()
