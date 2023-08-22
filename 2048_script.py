#!/usr/bin/env python3
# 2048_script.py — An exercise in web automation.
# For more information, see README.md

import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def open_site(site, moves):
    """Opens 2048 game site."""
    driver = webdriver.Safari()
    driver.set_window_size(1300, 1300)
    driver.get(site)
    push_button = WebDriverWait(driver, 0.01).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "container"))
    )
    for _ in range(moves):
        push_button.send_keys(Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
    return driver


def final_score(browser):
    """Calculates final score and closes browser."""
    score_field = browser.find_element(By.CLASS_NAME, "score-container")
    score = score_field.text
    split_score = score.split("+")
    # time.sleep(10)
    browser.close()
    return split_score[0]


def main():
    site_open = open_site(
        "https://play2048.co",
        int(input("How times would you like the loop to execute? ")),
    )
    # get_score = play_2048(site_open, loop_moves)
    print(f"You scored {final_score(site_open)}.")

    # while True:
    #     play_again = input("Would you like to play again? ").lower()
    #     if play_again == "yes":
    #         site_open = open_site(website)
    #         get_score = play_2048(site_open, loop_moves)
    #         print(f"You scored {final_score(get_score)}.")
    #     else:
    #         break


if __name__ == "__main__":
    main()
