import threading
import time
from settings import *

# Criação do semáforo
semaphore_1 = threading.Semaphore(2)
semaphore_2 = threading.Semaphore(2)

# Criação dos mutexes
mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex3 = threading.Lock()
mutex4 = threading.Lock()
mutex5 = threading.Lock()

# Classe do trem
class Train(threading.Thread):
    def __init__(self, name, color, x, y, endx, endy,event):
        threading.Thread.__init__(self)
        self.color = color
        self.name = name
        self.x = x
        self.y = y
        self.xStart = x
        self.yStart = y
        self.xEnd = self.xStart + endx
        self.yEnd = self.yStart + endy
        self.speed = 50.0
        self.event = event

    def run(self):
        while True:
            self.test()
            self.move()
            if self.event.is_set():
                break

    def setSpeed(self, speed):
        self.speed = speed

    def move(self):
        if self.x < self.xEnd and self.y == self.yStart:
            self.x += STEP
        elif self.x == self.xEnd and self.y < self.yEnd:
            self.y += STEP
        elif self.x > self.xStart and self.y == self.yEnd:
            self.x -= STEP
        else:
            self.y -= STEP
        time.sleep(1/self.speed)

    def test(self):
        match self.name:
            case "T1":
                #L1
                #L2
                #L3
                if self.x == self.xEnd and self.y == self.yEnd:
                    semaphore_1.acquire()
                    mutex2.acquire()
                #L4
                if self.x == 200 and self.y == self.yEnd:
                    mutex1.acquire()
                    semaphore_1.release()
                    if mutex2.locked():
                        mutex2.release()
                #L5
                if self.x == self.xStart and self.y == self.yStart:
                    if mutex1.locked():
                        mutex1.release()
            
            case "T2":
                if self.x == self.xStart and self.y == self.yStart:
                    semaphore_1.acquire()
                    mutex1.acquire()
                if self.x == self.xEnd and self.y and self.yStart:
                    semaphore_1.release()
                    if mutex1.locked():
                        mutex1.release()
                #daqui para baixo é baixo
                if self.x == self.xStart and self.x == self.y == self.yStart:
                    semaphore_2.acquire()
                    mutex5.acquire()
                if self.x == self.xEnd and self.y == self.yEnd:
                    mutex3.acquire()
                    semaphore_2.release()
                    if mutex5.locked():
                        mutex5.release()
                if self.x == self.xStart and self.y == self.yEnd:
                    if mutex3.locked():
                        mutex3.release()

            case "T3":
                if self.x == self.xStart and self.y == self.yStart:
                    semaphore_1.acquire()
                    mutex2.acquire()
                if self.x == self.xEnd and self.y == self.yEnd:
                    semaphore_1.release()
                    if mutex2.locked():
                        mutex2.release()
                #daqui para baixo é baixo
                if self.x == self.xEnd and self.y == self.yEnd:
                    semaphore_2.acquire()
                    mutex4.acquire()
                if self.x == self.xStart and self.y == self.yEnd:
                    mutex5.acquire()
                    semaphore_2.release()
                    if mutex4.locked():
                        mutex4.release()
                if self.x == self.xStart and self.y == self.yStart:
                    if mutex5.locked():
                        mutex5.release()

            case "T4":
                if self.x == self.xStart and self.y == self.yStart:
                    semaphore_2.acquire()
                    mutex3.acquire()
                if self.x == 200 and self.y == self.yStart:
                    mutex4.acquire()
                    semaphore_2.release()
                    if mutex3.locked():
                        mutex3.release()
                if self.x == self.xEnd and self.y == self.yEnd:
                    if mutex4.locked():
                        mutex4.release()