from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *

'''
/html/body/modal-container/div/div/div/div[4]/div[1]/rating/span/span[10]/button
для нажатия на 5 звезд

/html/body/modal-container/div/div/div/div[4]/app-tags-input/div/div[1]
для нажатия на кнопку "все супер"

/html/body/modal-container/div/div/div/div[4]/div[4]/button
для нажатия "продолжить"

/html/body/modal-container/div/div
само окно с оцениванием

/html/body/modal-container/div/div/div/div[4]/div[4]/button[2]
кнопка отправить
'''

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 99999)
driver.get(url)

time.sleep(1)

login_get = driver.find_element(By.ID, 'username')
password_get = driver.find_element(By.ID, 'password')
button_check = driver.find_element(By.XPATH, '/html/body/mystat/ng-component/ng-component/section/div/div/div/div/div[1]/tabset/div/tab[1]/form/button')

login_get.send_keys(username)
password_get.send_keys(password)
button_check.click()

time.sleep(1)

x_check = driver.find_element(By.XPATH, '/html/body/modal-container')
x_check.click()

time.sleep(2)

def register():
    element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/modal-container/div/div')))
    while element:
        time.sleep(0.3)

        five_star = driver.find_element(By.XPATH, '/html/body/modal-container/div/div/div/div[4]/div[1]/rating/span/span[10]/button')
        five_star.click()

        time.sleep(0.3)

        super_sign = driver.find_element(By.XPATH, '/html/body/modal-container/div/div/div/div[4]/app-tags-input/div/div[1]')
        super_sign.click()

        time.sleep(0.3)

        vote_button_check = driver.find_element(By.XPATH, '/html/body/modal-container/div/div/div/div[4]/div[4]/button')
        vote_button_check.click()

        time.sleep(1)

        five_star = driver.find_element(By.XPATH,'/html/body/modal-container/div/div/div/div[4]/div[1]/rating/span/span[10]/button')
        five_star.click()

        time.sleep(0.3)

        super_sign = driver.find_element(By.XPATH,'/html/body/modal-container/div/div/div/div[4]/app-tags-input/div/div[1]')
        super_sign.click()

        time.sleep(0.3)

        upload_vote_button = driver.find_element(By.XPATH, '/html/body/modal-container/div/div/div/div[4]/div[4]/button[2]')
        upload_vote_button.click()

        time.sleep(1)

register()