import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class SignIn(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.bitexen.com/")
        self.driver.implicitly_wait(10)

    def test_login(self):

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("correctUsername@gmail.com")
        self.driver.find_element_by_id("password").send_keys("wrongPassword")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()

        x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[4]/div").text
        print("Giriş yapılamadı. " + x)
        self.assertEqual(x, "Kullanıcı adı ya da şifre hatalı.")

        self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("wrongUsername@gmail.com")
        self.driver.find_element_by_id("password").send_keys("abcdeg32")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[4]/div").text
        print("Giriş yapılamadı. " + x)
        self.assertEqual(x, "Customer not found.")

        self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("invalidUsername")
        self.driver.find_element_by_id("password").send_keys("abc")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()

        x = self.driver.find_element(By.ID, "userName-helper-text").text
        print("Giriş yapılamadı. " + x)
        self.assertEqual(x, "Geçersiz e-posta adresi")

        self.driver.execute_script("window.history.go(-1)")
        self.driver.refresh()

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("correnctUsername@gmail.com")
        self.driver.find_element_by_id("password").send_keys("correctPassword")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()

        x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[2]/div/div/div[2]").text
        print(x)
        self.assertEqual(x, "Hoş geldin,")