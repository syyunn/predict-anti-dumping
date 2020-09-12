"""
Control based crawler
"""

import pyautogui
import pandas as pd
import time

from os import listdir
from os.path import isfile, join

from tqdm import tqdm

petitions_dir = './data/petitions'
htmls = [f.replace('.htm', '') for f in listdir(petitions_dir) if isfile(join(petitions_dir, f))]

# For debug-use only
# screenWidth, screenHeight = pyautogui.size()
# currentMouseX, currentMouseY = pyautogui.position()

case_list = './antidumping_us_itc_case_list.csv'
df = pd.read_csv(case_list)

cases = df['Case Number'].tolist()

for case in tqdm(cases):
    if case not in htmls:
        # Click case number slot
        case_number_pos = 2212, 336
        pyautogui.click(case_number_pos[0], case_number_pos[1])
        pyautogui.click()  # to make sure we click twice

        # Delete previous case_number
        time.sleep(1)
        pyautogui.press("right", presses=15)
        pyautogui.press("backspace", presses=30, interval=0.05)


        # Type case_number in
        pyautogui.write(case)


        search_button = 2237, 989
        pyautogui.click(search_button[0], search_button[1])
        pyautogui.click(search_button[0], search_button[1])

        time.sleep(6.5)

        pyautogui.moveTo(2195, 202)
        pyautogui.click(button="right")
        pyautogui.move(55, 85)
        pyautogui.click()

        # type case_number as filename to save
        time.sleep(2)
        pyautogui.write(case)
        pyautogui.press("return")

        # go-back
        go_back = 1813, 85
        pyautogui.click(go_back[0], go_back[1])
        time.sleep(3)


if __name__ == "__main__":
    pass
