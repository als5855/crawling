from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def run():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://koritbs.cafe24.com/student/index.php")
    driver.maximize_window()
    sleep(2)

    loginId = driver.find_element(by=By.CSS_SELECTOR, value='body > div > form > table > tbody > tr:nth-child(3) > td > input')
    loginId.send_keys("wlals5855")
    sleep(1)

    loginPw = driver.find_element(by=By.CSS_SELECTOR, value='body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-0.border-top-0.bg-brown > td > input')
    loginPw.send_keys("dnfru9630!@")
    sleep(1)

    loginBtn = driver.find_element(by=By.CSS_SELECTOR, value='body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-danger.border-top-0.bg-brown > td > div > div:nth-child(2) > button')
    loginBtn.click()
    sleep(1)

    SelectBtn = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr.hover.pointer')
    SelectBtn.click()
    sleep(1)

    crawlingBtn = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > ul > li:nth-child(10) > div')
    crawlingBtn.click()
    sleep(1)

    postBtn = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > caption > div > div:nth-child(2) > div > a')
    postBtn.click()
    sleep(1)

    postTitleInput = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input')
    postTitleInput.send_keys("장지민")
    sleep(1)

    postContentInput = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div.ck.ck-editor__main > div')
    postContentInput.send_keys("게시글 등록하기 완료")
    sleep(1)

    postComplete = driver.find_element(by=By.CSS_SELECTOR, value='body > table > tbody > tr:nth-child(2) > td:nth-child(2) > form > table > tbody > tr.end > td > button')
    postComplete.click()
    sleep(1)




