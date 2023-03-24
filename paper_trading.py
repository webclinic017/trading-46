from importlib.resources import path
from unittest import result
import PIL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import re
from pathlib import Path 
from urllib.request import urlretrieve
from time import sleep
from PIL import Image
import pyocr
import pyocr.builders
import pytesseract
import cv2
import PIL.ImageDraw
import operator
from PIL import *
from soupsieve import select
from pathlib import Path
import sys,os
import subprocess
import shutil
username = "richard.u15@gmail.com"
password = "Oscar89060815"
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
