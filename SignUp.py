from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time


class SignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.bitexen.com/")

    def test_signup(self):

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys("berkyalinkilic@gmail.com")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys("İbrahim")
        self.driver.find_element_by_id("surname").send_keys("Yalınkılıç")
        self.driver.find_element_by_id("password").send_keys("asparas1")
        self.driver.find_element_by_id("password2").send_keys("asparas1")
        self.driver.find_element_by_id("referrerCode").send_keys("")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        self. driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        time.sleep(2)
        x = self.driver.find_element(By.XPATH,"//*[@id='root']/div/div[3]/div[9]/div").text
        print(x)
        self.assertEqual(x, 'Kullanıcı zaten mevcut.')

        self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys("berkyalinkilic")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys("İbrahim")
        self.driver.find_element_by_id("surname").send_keys("Yalınkılıç")
        self.driver.find_element_by_id("password").send_keys("asparas1")
        self.driver.find_element_by_id("password2").send_keys("asparas1")
        self.driver.find_element_by_id("referrerCode").send_keys("")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        time.sleep(2)
        x = self.driver.find_element(By.ID,"userName-helper-text").text
        print(x)
        self.assertEqual(x, 'Geçersiz e-posta adresi')

        self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys("berkyalinkilic@gmail.com")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys("İbrahim")
        self.driver.find_element_by_id("surname").send_keys("Yalınkılıç")
        self.driver.find_element_by_id("password").send_keys("")
        self.driver.find_element_by_id("password2").send_keys("")
        self.driver.find_element_by_id("referrerCode").send_keys("")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        time.sleep(2)
        x = self.driver.find_element(By.ID, "password-helper-text").text
        print(x)
        self.assertEqual(x, 'Boş bırakılamaz')

        self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()


        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys("berkyalinkilic@gmail.com")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys("İbrahim")
        self.driver.find_element_by_id("surname").send_keys("Yalınkılıç")
        self.driver.find_element_by_id("password").send_keys("asparas1")
        self.driver.find_element_by_id("password2").send_keys("asparas11")
        self.driver.find_element_by_id("referrerCode").send_keys("")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        time.sleep(2)
        x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[9]/div").text
        print(x)
        self.assertEqual(x, 'Girdiğiniz şifreler eşleşmiyor')



