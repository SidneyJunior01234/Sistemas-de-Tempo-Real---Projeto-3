import threading
import time
from settings import *

# Criação do semáforo
#semaphore_1 = threading.Semaphore(1)
#semaphore_2 = threading.Semaphore(1)

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
                    mutex1.acquire()
                    mutex2.acquire()
                #L4
                if self.x == 200 and self.y == self.yEnd:
                    if mutex2.locked():
                        mutex2.release()
                #L5
                if self.x == self.xStart and self.y == self.yStart:
                    if mutex1.locked():
                        mutex1.release()
            
            case "T2":
                #L6
                if self.x == self.xStart and self.y == self.yStart:
                    mutex1.acquire()
                #L5
                if self.x == self.xEnd-TRAIN_WIDTH and self.y and self.yStart:
                    if not mutex3.locked():
                        mutex3.acquire()
                    if mutex1.locked():
                        mutex1.release()
                #L7
                if self.x == self.xEnd and self.y == self.yEnd:
                    mutex4.acquire()
                    if mutex3.locked():
                        mutex3.release()
                #L8
                if self.x == self.xStart and self.y == self.yEnd:
                    if mutex4.locked():
                        mutex4.release()

            case "T3":
                #L9
                if self.x == self.xEnd and self.y == self.yEnd:
                    mutex5.acquire()
                #L10
                if self.x == self.xStart+TRAIN_WIDTH and self.y == self.yEnd:
                    mutex3.acquire()
                    if mutex5.locked():
                        mutex5.release()
                #L7
                if self.x == self.xStart and self.y == self.yStart:
                    mutex2.acquire()
                    if mutex3.locked():
                        mutex3.release()
                #L4
                if self.x == self.xEnd and self.y == self.yStart:
                    if mutex2.locked():
                        mutex2.release()

            case "T4":
                #L11
                if self.x == self.xStart and self.y == self.yStart:
                    mutex5.acquire()
                    mutex4.acquire()
                #L8
                if self.x == 200 and self.y == self.yStart:
                   if mutex4.locked():
                    mutex4.release()
                #L10
                if self.x == self.xEnd and self.y == self.yEnd:
                   if mutex5.locked():
                    mutex5.release()
                #L12
                #L13
