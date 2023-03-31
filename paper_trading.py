from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path 
from time import sleep



# define your username and password
# note that you need to have a CMoney account and disable 2 factor authentication in order to use this script
# also note that you need to have a chromedriver.exe that is compatible with your chrome version
# you can download it from https://chromedriver.chromium.org/downloads

username = ""
password = ""

class CMoneyAutoTrading:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless"); 
    driver = webdriver.Chrome(executable_path=('./chromedriver.exe'), options=options)
    driver.get('https://www.cmoney.tw/member/login/')
    driver.find_element_by_id('Account').send_keys(username)
    driver.find_element_by_id('Password').send_keys(password)
    driver.find_element_by_id('RememberMe').click()
    driver.find_element_by_id('Login').click()
    driver.get('https://www.cmoney.tw/vt/qa.aspx')
    driver.find_element_by_class_name('user__itemCntr').click()
    driver.get('https://www.cmoney.tw/vt/main-page.aspx?aid=1303340')


    
    while True:
        try:
            driver.find_element_by_id('textBoxCommkey').send_keys('0056')
            driver.find_element_by_id('TextBoxQty').send_keys('1')
            driver.find_element_by_id('TextBoxPrice').send_keys('28.18')

            driver.find_element_by_id('TextBoxPrice').clear()
            driver.find_element_by_id('TextBoxPrice').send_keys('28')
            sleep(0.1)
            driver.find_element_by_id('Orderbtn').click()
            driver.close()
            break
        except:
            pass
    # sleep(30)


# driver.find_element_by_xpath('//*[@title="小資族"]').click()
