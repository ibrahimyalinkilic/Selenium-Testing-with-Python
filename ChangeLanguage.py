import unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://dev.bitexen.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_english(self):

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("username@gmail.com")
        self.driver.find_element_by_id("password").send_keys("password")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[5]/div[2]/div").click()
        self.driver.find_element_by_xpath("//*[@id='menu-']/div[3]/ul/li[2]").click()
        x = self.driver.find_element_by_id("language").get_attribute("value")
        print("Language = " + x)
        self.assertEqual(x, "en")
        time.sleep(2)

    def test_turkish(self):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("username@gmail.com")
        self.driver.find_element_by_id("password").send_keys("password")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[5]/div[2]/div").click()
        self.driver.find_element_by_xpath("//*[@id='menu-']/div[3]/ul/li[1]").click()
        time.sleep(2)
        x = self.driver.find_element_by_id("language").get_attribute("value")
        print("Language = " + x)
        self.assertEqual(x, "tr")

    def tearDown(self):

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
