import pyautogui
import time

from zmq import HELLO_MSG
time.sleep(2)

for i in range(0,15):
    pyautogui.typewrite("Hello")
    time.sleep(2)
    pyautogui.press("enter")