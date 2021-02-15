"""Author: Connor McNab"""
# Turns out that distrokid doesnt count  duplicate votes from the same device but oh well this was fun
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import threading


# Initialises the bot
class VoteBot:
    def __init__(self):
        try:  # Attempts to load driver and returns Error if it is not found
            self.driver = webdriver.Chrome("chromedriver.exe")
            self.vote()
        except FileNotFoundError:
            print("Could not locate driver.")

    # Loads webpage and searches for vote button and clicks
    def vote(self):
        self.driver.get("https://distrokid.com/spotlight/{band}/vote/")  # Loads webpage
        try:  # Tries to load and find element, uses the wait function to ensure the page loads before checking
            self.element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((
                    By.XPATH, '{XPATH id}')))
            self.element.click()  # Clicks on element
            time.sleep(2)  # Ensures link request goes through before closing the window
        finally:
            self.driver.close()  # Closes the window


# Multi threading to make it faster
while True:  # Runs until manually stopped
    threads = list()  # Creates a list that threading jobs will be added to
    for i in range(4):  # Limits amount of bots/windows open to 4 to stop computer from dying
        thread = threading.Thread(target=VoteBot, daemon=True)  # Creates thread
        threads.append(thread)  # Appends thread to the list
        thread.start()  # Starts thread

    for i, thread in enumerate(threads):  # Joins threads
        thread.join()
