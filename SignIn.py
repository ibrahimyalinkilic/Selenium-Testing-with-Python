from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://dev.bitexen.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()

time.sleep(2)
print("Giriş yap butonuna basıldı.")

mail = input("Giriş yapmak için mailinizi giriniz: ")
driver.find_element_by_id("userName").send_keys(mail)
print("Mail adresiniz girildi. ")
time.sleep(1)

password = input("Giriş yapmak için şifrenizi giriniz: ")
driver.find_element_by_id("password").send_keys(password)
print("Şifreniz girildi. ")
time.sleep(1)

driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
print("Giriş yapılıyor...")
