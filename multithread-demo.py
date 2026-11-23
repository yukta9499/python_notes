from threading import Thread
def task():
    print("thread is running")
#create thread
t = Thread(target=task)

#start thread
t.start()

#waiting for completion
t.join()
print("Main program ends")
