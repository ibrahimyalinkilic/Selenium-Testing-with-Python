from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://demo.guru99.com/test/radio.html")

time.sleep(2)


c1 = driver.find_element_by_xpath("//*[@id='vfb-6-0']")
c1.click()
print("Checkbox1 is selected.")
time.sleep(2)

c2 = driver.find_element_by_id("vfb-6-1")
c2.click()
print("Checkbox2 is selected.")
time.sleep(2)

c3 = driver.find_element_by_id("vfb-6-2")
c3.click()
print("Checkbox3 is selected.")
time.sleep(2)
c3.click()
print("Checkbox3 is cleared.")

time.sleep(2)

r1 = driver.find_element_by_id("vfb-7-2")
r1.click()
print("Option2 is selected.")

time.sleep(3)

driver.close()