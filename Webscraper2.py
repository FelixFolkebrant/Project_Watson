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


Dictionary = {}     #{[Date1 {Subject 1 : [name, starttine, endtime]]}

bruh = []


for x in range(1,100):
#Sub 1
    print(x)
    date = str(driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[2]/div/span[1]').text)
    try:
        name =      driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[1]/div[2]').text
        startTime = driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[3]').text
        endTime =   driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[2]').text
        bruh.append(name)
        bruh.append(startTime)
        bruh.append(endTime)
    except: 
        print("none")
#Sub 2
    try:
        name =      driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[4]/div[2]').text
        startTime = driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[6]').text
        endTime =   driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[5]').text
        bruh.append(name)
        bruh.append(startTime)
        bruh.append(endTime)
    except: 
        print("none")
#Sub 3
    try:
        name =      driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[7]/div[2]').text
        startTime = driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[9]').text
        endTime =   driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[8]').text
        bruh.append(name)
        bruh.append(startTime)
        bruh.append(endTime)
    except: 
        print("none")
#Sub 4
    try:
        name =      driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[10]/div[2]').text
        startTime = driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[12]').text
        endTime =   driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[11]').text
        bruh.append(name)
        bruh.append(startTime)
        bruh.append(endTime)
    except: 
        print("none")


print(bruh)
driver.quit()

# //*[@id="contents"]/div[1]/div[1]/div[3]/div[1]/div[2]
# //*[@id="contents"]/div[1]/div[1]/div[3]/div[8]
# //*[@id="contents"]/div[1]/div[1]/div[3]/div[9] 





# //*[@id="contents"]/div[1]/div[1]/div[3]/div[4]/div[2]
# //*[@id="contents"]/div[1]/div[1]/div[3]/div[7]/div[2]

# //*[@id="contents"]/div[1]/div[2]/div[3]/div[1]/div[2]
# //*[@id="contents"]/div[1]/div[2]/div[3]/div[4]/div[2]
# //*[@id="contents"]/div[1]/div[2]/div[3]/div[7]/div[2]
# //*[@id="contents"]/div[1]/div[2]/div[3]/div[10]/div[2]