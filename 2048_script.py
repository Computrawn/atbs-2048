#! python3
# 2048_script.py — An exercise in web automation.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def open_site(site):
    """Opens 2048 game site."""
    browser = webdriver.Safari()
    browser.get(site)
    time.sleep(pause_time)
    return browser


def play_2048(browser):
    """Sends up, right, down left commands."""
    push_button = browser.find_element_by_class_name("container")
    push_button.send_keys(Keys.UP)
    time.sleep(pause_time)
    push_button.send_keys(Keys.RIGHT)
    time.sleep(pause_time)
    push_button.send_keys(Keys.DOWN)
    time.sleep(pause_time)
    push_button.send_keys(Keys.LEFT)
    time.sleep(pause_time)


website = "https://play2048.co"
pause_time = 1
# play_moves = int(input("How moves would you like to make? "))

site_open = open_site(website)
play_2048(site_open)
