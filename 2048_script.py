#!/usr/bin/env python3
# 2048_script.py — An exercise in web automation.
# For more information, see README.md

import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


PAUSE = 0.001


def open_site(site):
    """Opens 2048 game site."""
    browser = webdriver.Safari()
    browser.get(site)
    browser.set_window_size(1300, 1300)
    return browser


def play_2048(browser, loop_moves):
    """Plays game by sending loop of direction commands."""
    push_button = browser.find_element(By.CLASS_NAME, "container")
    for _ in range(loop_moves):
        push_button.send_keys(Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
        time.sleep(PAUSE)
    return browser


def final_score(browser):
    """Calculates final score and closes browser."""
    score_field = browser.find_element(By.CLASS_NAME, "score-container")
    score = score_field.text
    split_score = score.split("+")
    # time.sleep(10)
    browser.close()
    return split_score[0]


def main():
    website = "https://play2048.co"
    loop_moves = int(input("How times would you like the loop to execute? "))

    site_open = open_site(website)
    get_score = play_2048(site_open, loop_moves)
    print(f"You scored {final_score(get_score)}.")

    while True:
        play_again = input("Would you like to play again? ").lower()
        if play_again == "yes":
            site_open = open_site(website)
            get_score = play_2048(site_open, loop_moves)
            print(f"You scored {final_score(get_score)}.")
        else:
            break


if __name__ == "__main__":
    main()
