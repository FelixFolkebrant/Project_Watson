from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import datetime


HideWindow = False
PATH = "C:\Program Files (x86)\chromedriver.exe"    #Ändra den här till din egen path (Sök på chromedriver och ladda ner den verisionen som stämmer med den chrome du har nedladdat)
startTime = int(time.time())
driver = webdriver.Chrome(PATH)
if HideWindow:
    driver.set_window_position(-2000, 0)
driver.get('https://cloud.timeedit.net/abbindustrigymnasium/web/public1/ri1Y7X3QQQfZY6QfZ5073515y7Y7.html')

d = {}     #{[Date1 {Subject 1 : [name, starttine, endtime]]}





# date = [str(driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[1]/div[2]/div/span[1]').text),str(driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[2]/div[2]/div/span[1]').text)]
date = str(driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[1]/div[2]/div/span[1]').text)
Subject = "Subject 1"
# d['date'][
#     driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[1]/div[3]/div[1]/div[2]').text
#     ,driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[1]/div[3]/div[3]').text
#     ,driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[1]/div[3]/div[2]').text
#     ]
d["kuk"]= "kukiballen"

print(d)
driver.quit()