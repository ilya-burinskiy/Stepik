from threading import Semaphore, Thread
from collections import deque
import portion

class Package:

    def __init__(self, arrive, duration):
        self.tarrive = arrive
        self.tduration = duration
        self.tprocessed = -1

    def __repr__(self):
        return repr((self.tarrive, self.tduration, self.tprocessed))

def package_producer(packages):
    global empty, full, time_sem, buff, t, isfinished

    empty.acquire()
    while len(buff) != buff.maxlen:
        buff.append(packages.popleft())
    if len(packages) == 0:
        isfinished = True
    full.release()
    prev_time = None
    while len(packages) != 0:
        time_sem.acquire()
        time = t

        p = packages.popleft()
        empty.acquire()

        if p.tarrive >= time:
            buff.append(p)

        elif prev_time is not None:
            if (prev_time < p.tarrive) and (p.tarrive < time):
                buff.append(p)

        if len(packages) == 0:
            isfinished = True
        full.release()
        prev_time = time


    

def package_consumer():
    global empty, full, time_sem, buff, t, isfinished

    while not isfinished:
        full.acquire()
        if len(buff) != 0:
            p = buff.popleft()
            empty.release()
            
            if p.tarrive > t:
                t = p.tarrive
            p.tprocessed = t
            t += p.tduration
            time_sem.release()

    while len(buff) != 0:
        p = buff.popleft()
        if p.tarrive > t:
            t = p.tarrive
        p.tprocessed = t
        t += p.tduration

if __name__ == "__main__":
    
    qsize, p_num = map(int, input().split())
    packages = []

    for i in range(p_num):
        arr, dur = map(int, input().split())
        packages.append(Package(arr, dur))

    buff = deque([], maxlen=qsize)
    empty = Semaphore(1)
    full = Semaphore(0)
    time_sem = Semaphore(0)
    isfinished = False

    if len(packages) > 0:
        t = packages[0].tarrive
        thr1 = Thread(target=package_producer, 
                      args=(deque(packages.copy(), maxlen=p_num), ))
        thr2 = Thread(target=package_consumer)

        thr1.start()
        thr2.start()

        thr1.join()
        thr2.join()

        for p in packages:
            print(p.tprocessed)
