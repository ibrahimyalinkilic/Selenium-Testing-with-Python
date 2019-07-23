from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://dev.bitexen.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

x = driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]")
x.click()

time.sleep(2)


print("Hesap oluştur butonuna basıldı.")
time.sleep(1)

mail = input("Hesabınızı oluşturmak için bir mail adresi giriniz:")
driver.find_element_by_id("userName").send_keys(mail)
print("Kullanıcı oluşturmak için mail girildi.")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()

name = input("Adınızı giriniz:")
driver.find_element_by_id("name").send_keys(name)
print("İsim girildi.")
time.sleep(1)
surname = input("Soyadınızı giriniz:")
driver.find_element_by_id("surname").send_keys(surname)
print("Soyisim girildi.")
time.sleep(1)
password = input("Şifrenizi giriniz:")
driver.find_element_by_id("password").send_keys(password)
print("Şifre girildi.")
time.sleep(1)
driver.find_element_by_id("password2").send_keys(password)
print("Şifre tekrar girildi.")
time.sleep(2)
driver.find_element_by_id("referrerCode").send_keys("")
driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()