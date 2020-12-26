
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://banssb.ucy.ac.cy:9091/PRODel-CY/twbkwbis.P_WWWLogin")
UserID = driver.find_element_by_id("UserID")
UserID.send_keys("NO!")
PIN = driver.find_element_by_name("PIN")
PIN.send_keys("NO!")
Submit = driver.find_element_by_xpath("/html/body/div[3]/form/p/input")
Submit.click()
AkadStix = driver.find_element_by_xpath("/html/body/div[3]/table[2]/tbody/tr[2]/td[2]/a")
AkadStix.click()
Eggrafes = driver.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[1]/td[2]/a")
Eggrafes.click()
ProsthAfairMath = driver.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[2]/td[2]/a")
ProsthAfairMath.click()
Eksamino = driver.find_element_by_xpath("/html/body/div[3]/form/input")
Eksamino.click()

def start():
    while 1:
        try:
            Mam1 = driver.find_element_by_id("crn_id1")
            Mam1.send_keys("10623")  # 211

            mam9 = driver.find_element_by_id("crn_id2")
            mam9.send_keys(Keys.ENTER)
            time.sleep(4)
            exit(0)

        except NoSuchElementException:
            driver.refresh()
            continue


start()
