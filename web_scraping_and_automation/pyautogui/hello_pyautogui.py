# YouTube Video: https://www.youtube.com/watch?v=dUeCoUw9OoQ
import pyautogui
import time

time.sleep(5)
pyautogui.click()
distance = 400
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance = distance - 50
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance = distance - 50
    pyautogui.dragRel(0, -distance, duration=0.2)
