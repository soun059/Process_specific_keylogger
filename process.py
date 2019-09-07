from win32 import win32gui

import time

import psutil

from win32 import win32process
from pynput.keyboard import Key, Listener
import multiprocessing
#import logging



def proces():
    i=0
    kut = ""
    #while i <= 1:

    time.sleep(1)

    w=win32gui

    w.GetWindowText (w.GetForegroundWindow())

    pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())

    kut = psutil.Process(pid[-1]).name()
    print(kut)
    if(kut == "vlc.exe"):
        listen()
    else:
        proces()


def ket(key):
    global kut
    print(key)
    if key == Key.space :
        print("Space has been pressed")



def listen():
    with Listener(on_press=ket) as listener:
        listener.join()
    proces()

proces()

##if __name__ == '__main__':
##    p1 = multiprocessing.Process(target = proces)
##    p2 = multiprocessing.Process(target = listen)
##    p1.start()
##    p2.start()











