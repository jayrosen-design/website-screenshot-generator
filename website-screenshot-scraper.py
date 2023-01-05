import csv
import os
import time
import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver

def capture_screenshot(url, filename):
  # Set up a webdriver to take a screenshot
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  driver = webdriver.Chrome(chrome_options=options)
  driver.get(url)

  # Set the window size to 1920x1080
  driver.set_window_size(1920, 1080)

  # Wait for the page to load
  time.sleep(3)


  # Take the screenshot and save it to the current directory
  screenshot = driver.save_screenshot(f'{filename}.png')
  driver.quit()

def main():
  # Open the CSV file of websites
  with open('websites.csv', 'r') as file:
    reader = csv.reader(file)

    # Iterate through each row in the CSV
    for row in reader:
      url = row[0]
      filename = row[1]

      # website screenshot
      capture_screenshot(url, filename)

if __name__ == '__main__':
  main()

