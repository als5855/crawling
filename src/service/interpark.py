from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def run():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.interpark.com/")
    sleep()