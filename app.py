import pyautogui
import keyboard
import time

time.sleep(5)

while True:
    pyautogui.click()
    if keyboard.is_pressed('q'):
        break