import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class SignIn(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.bitexen.com/")

    def test_login(self):

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("berkyalinkilic@gmail.com")
        self.driver.find_element_by_id("password").send_keys("asparas11")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        time.sleep(1)
        x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[4]/div").text
        print(x)
        self.assertEqual(x, "Kullanıcı adı ya da şifre hatalı.")

        self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("berkyalinkilicc@gmail.com")
        self.driver.find_element_by_id("password").send_keys("asparas1")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        time.sleep(1)
        x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[4]/div").text
        print(x)
        self.assertEqual(x, "Customer not found.")

        self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("abc")
        self.driver.find_element_by_id("password").send_keys("abc")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        time.sleep(1)
        x = self.driver.find_element(By.ID, "userName-helper-text").text
        print(x)
        self.assertEqual(x, "Geçersiz e-posta adresi")

        self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("berkyalinkilic@gmail.com")
        self.driver.find_element_by_id("password").send_keys("asparas1")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        time.sleep(2)
        x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[2]/div/div/div[2]").text
        print(x)
        self.assertEqual(x, "Hoş geldin,")