# YouTube Video: https://www.youtube.com/watch?v=4rgt7Od7-KM
# Thanks to Al Swiegart and his excellent book:
# Automating the Boring Stuff with Python for writing this module 
# and also for inspiration for pyautogui illustrative purposes.

import pyautogui

# Depending on your program, pyautogui can "go rogue". As a failsafe, 
# we may move the mouse to the upper left corner of the screen to 
# halt the execution of a "rogue" program by setting the following:
pyautogui.FAILSAFE = True

# The location of the mouse cursor is provided as an (x,y) pair. 
# This value of x and y are determined by the resolution of your
# monitor. My resolution is 2720x1024. For example:
#   The top right corner of my screen is (2720, 0)
#   The bottom left corner of my screen is (0, 1024),
#   etc.

# You can obtain the coordinates of your own computer screen here:
print(pyautogui.size())

# Moving the mouse to a specifc location:
pyautogui.moveTo(100, 100, duration=0.25)

# Moving the mouse to specific locations (in a loop):
# Try running this program, but then also try moving the
# mouse up and to the left to see the result of the failsafe
# we previously enabled. 
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

# Move the mouse relative to a specific location:
# Run this line a couple times to see the effect.
pyautogui.moveRel(100, 0, duration=0.25)

# Alternatively, we can simply stick this in a
# loop as well to see the result.
for i in range(5):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)

# Getting the mouse position:
print(pyautogui.position())

# Clicking the mouse:
# The "click" function takes two arguments (x,y) that
# correspond to the (x,y) positions on the screen.
# For example:
pyautogui.click(100, 100)

# Click the location of the "Terminal" menu item in terminal:
pyautogui.click(187, 33)

# Dragging the mouse (moving the mouse while simultaneously clicking).
# moveTo and moveRel have dragging parallels:
# dragTo and dragRel
# Example drag the "Projects" folder on Desktop.
pyautogui.dragTo(200,211,duration=0.25)


# Scrolling the mouse:
# Tell pyautogui how many "units" to scroll up or down.
pyautogui.scroll(200)

