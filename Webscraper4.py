from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

HideWindow = False
PATH = "C:\Program Files (x86)\chromedriver.exe"    #Ändra den här till din egen path (Sök på chromedriver och ladda ner den verisionen som stämmer med den chrome du har nedladdat)
startTime = int(time.time())
driver = webdriver.Chrome(PATH)
if HideWindow:
    driver.set_window_position(-2000, 0)
driver.get('https://cloud.timeedit.net/abbindustrigymnasium/web/public1/ri1Y7X3QQQfZY6QfZ5073515y7Y7.html')

Subject = []
D = {}     #{[Date1 {Subject 1 : [name, starttine, endtime]]}
Xpa = [1, 4, 7, 10, 13, ]
for x in range(1,100):

#Sub 1
    try:
        print(x)
#Försök hitta datumet
        date = str(driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[2]/div/span[1]').text)
        for y in Xpa:
            try:
#Försök hitta namnet på lektionen
                name = driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[{y}]/div[2]').text
                extra = driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[{y}]/div[3]').text
                #Om det är moderna eller ngåon annan lektion vi inte har så iggar vi
                if "Moderna språk" in name:
                    print("Ignored Subject")
                #Om det är Gemensam aktivitet checkar vi om det är Studieverstad (igga) eller något annat
                elif "Gem aktivitet" in name:
                    if extra == "STUDIEVERKSTAD":
                        print("Studieverkstad Iggad bror")
                    else:
                        Subject.append([
                        driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[{y}]/div[3]').text,       #Tar nästa sak istället för Gem Aktivitet
                        driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[{y+2}]').text,
                        driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[{y+1}]').text
                        ])

                else:
                    Subject.append([
                        driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[{y}]/div[2]').text,
                        driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[{y+2}]').text,
                        driver.find_element_by_xpath(f'//*[@id="contents"]/div[1]/div[{x}]/div[3]/div[{y+1}]').text
                        ])
                    if "PROV" in extra:
                        Subject.append(extra)
                        print("PROV WAS ADDED")
            except: 
                print("none")
        D[date] = Subject
        Subject = []
    except:
        print("Date unavailable")

print(Subject)

print(json.dumps(D,sort_keys=True, indent=4))
driver.quit()
with open('TimeEdit.json', 'w', encoding='utf-8') as f:
    json.dump(D, f, ensure_ascii=False, indent=4)
# //*[@id="contents"]/div[1]/div[1]/div[3]/div[1]/div[2]
# //*[@id="contents"]/div[1]/div[1]/div[3]/div[8]
# //*[@id="contents"]/div[1]/div[1]/div[3]/div[9] 





# //*[@id="contents"]/div[1]/div[1]/div[3]/div[4]/div[2]
# //*[@id="contents"]/div[1]/div[1]/div[3]/div[7]/div[2]

# //*[@id="contents"]/div[1]/div[2]/div[3]/div[1]/div[2]
# //*[@id="contents"]/div[1]/div[2]/div[3]/div[4]/div[2]
# //*[@id="contents"]/div[1]/div[2]/div[3]/div[7]/div[2]
# //*[@id="contents"]/div[1]/div[2]/div[3]/div[10]/div[2]