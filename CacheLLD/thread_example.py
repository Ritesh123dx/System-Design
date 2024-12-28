from threading import Thread, Lock
import time

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count = self.count + 1


class MyThread(Thread):
    lock_race = Lock()
    def __init__(self, counter):
        super().__init__()
        self.counter = counter
        
    
    def run(self):
        
        for i in range(100):
            with MyThread.lock_race:
                count = self.counter.count
                time.sleep(0.000008)
                self.counter.count = count + 1
                # print(self.counter.count)

            
    
    def print_value(self):
        print(self.counter.count)


counter = Counter()
thread1 = MyThread(counter)
thread2 = MyThread(counter)

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print(counter.count)



