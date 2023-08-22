#!/usr/bin/env python3
# 2048_script.py — An exercise in web automation.
# For more information, see README.md

import logging
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


def play_2048() -> int:
    """Opens, plays and closes 2048 game site in Safari then returns score."""
    driver = webdriver.Safari()
    driver.set_window_size(1300, 1300)
    driver.get("https://play2048.co")
    push_button = WebDriverWait(driver, 0.01).until(
        EC.presence_of_element_located((By.CLASS_NAME, "container"))
    )
    for _ in range(200):
        push_button.send_keys(Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)

    score_field = driver.find_element(By.CLASS_NAME, "score-container")
    score = score_field.text
    split_score = score.split("+")
    # driver.implicitly_wait(10)  # Wait 10 seconds
    score = split_score[0]
    driver.close()
    return int(score)


def main():
    score = play_2048()
    print(f"Your final score was: {score:,}.")


if __name__ == "__main__":
    main()
