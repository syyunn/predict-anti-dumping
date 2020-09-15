"""
Crawl All Tickers From NYSE Official Ticker Listings Directory
https://www.nyse.com/listings_directory/stock#
"""
import pyautogui
import pandas as pd
import time
from bs4 import BeautifulSoup
from tqdm import tqdm

# # For debug-use only
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

listings_position = 2790+20, 885
right_click_position = 2790+20, 858
save_as_margin = 50, 65

nyse_symbol_name_df = pd.DataFrame()

for page in tqdm(range(271, 655)):
    time.sleep(1)
    pyautogui.click(listings_position[0], listings_position[1])
    if page == 271:
        pyautogui.click()
    else:
        pass
    time.sleep(1)
    pyautogui.click(right_click_position[0], right_click_position[1], button="right")

    pyautogui.click(
        right_click_position[0] + save_as_margin[0],
        right_click_position[1] + save_as_margin[1],
    )
    save_as_title_position = 2755, 126
    pyautogui.click(save_as_title_position[0], save_as_title_position[1])
    time.sleep(1)
    pyautogui.press("right", presses=50)
    pyautogui.press(
        "backspace", presses=50,
    )
    pyautogui.write(str(page))
    pyautogui.press("return")
    time.sleep(1.5)
    with open(f"../data/nyse_stock_listings/{page}.htm") as f:
        bs = BeautifulSoup(f)
        paginated_as = bs.findAll("li", {"class": "disabled"})[0].text
        assert paginated_as == str(page), "page order broken"



if __name__ == "__main__":
    pass
