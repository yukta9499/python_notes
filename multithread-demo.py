# from threading import Thread
# def task():
#     print("Thread is running")
# #create thread
# t = Thread(target=task)         #target = func_name

# #start thread
# t.start()

# #waiting for completion
# t.join()

# print("Main program ends")


#2.
from threading import Thread
from time import sleep

def task():
    for i in range(3):
        print(i)
        sleep(i)
t= Thread(target=task)
t.start()
print("End of program")


#3
# from threading import Thread
# import time
# def numbers():
#     for i in range(1,6):
#         print(i)
#         time.sleep(1)
# def alphabets():
#     for ch in ['A',]
#         print(ch)
#         time.sleep(2)

# t1 = Thread(target=numbers)
# t2 = Thread(target=alphabets)
