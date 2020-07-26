import time
import threading

def test():
    print(time.ctime())
    threading.Timer(60,test).start()

#adding this comment just to make a commit
test()
