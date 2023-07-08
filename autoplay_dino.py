import pyautogui
from PIL import Image, ImageGrab
import numpy as np
from datetime import datetime, timedelta

def controller(action):
    if action.lower() == "jump":
        pyautogui.keyUp('down')
        pyautogui.press('up')
    elif action.lower() == "neil":
        pyautogui.keyDown('down')


def is_object_detected(image_array, theme_mode):
    print(theme_mode)
    image_array = np.array(image)
    pixel_values = {pixel_value for array in image_array.tolist() for pixel_value in set(array)}
    if theme_mode == 'dark':
        return True if any([pixel_value for pixel_value in pixel_values if pixel_value > 100]) else False
    else:
        return True if any([pixel_value for pixel_value in pixel_values if pixel_value < 40]) else False

time_gap = datetime.now() + timedelta(seconds=30) #increasing distance with respect to time

x = 650
__import__('time').sleep(2)
while True:
    if datetime.now() > time_gap:
        x = 800
    image = ImageGrab.grab(bbox=(500,624, x, 700)).convert('L') #taking screenshot & converting to grayscale.
    theme_mode = "light" if any([ pixel_value for pixel_value in {data for array in np.array(ImageGrab.grab(bbox=(1000,200, 1025, 225)).convert('L')).tolist() for data in set(array)} if pixel_value>=250]) else "dark"
    if is_object_detected(image, theme_mode):
        controller('jump')





