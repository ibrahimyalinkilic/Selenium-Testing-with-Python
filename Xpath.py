from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input").send_keys("abc")

ara = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[2]/div[2]/div[2]/center/input[1]")
time.sleep(2)
ara.click()

tikla = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div[1]/a/h3")
time.sleep(2)
tikla.click()

driver.close()