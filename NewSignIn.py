from selenium import webdriver
from selenium.webdriver.common.by import By


class login:

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.bitexen.com/")
        self.driver.implicitly_wait(5)


    #Tarayıcı kapama fonksiyonu
    def tearDown(self):

        self.driver.quit()


    # Başarılı giriş yapma testi
    def success_login(self, username, password):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        try:
            x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[2]/div/div/div[2]").text
            if x == "Hoş geldin,":
                print("success_login --->  " + "TEST BAŞARILI! Giriş yapıldı. " + "İstenilen hata mesajı alındı: " + x)

        except:
            print("success_login --->   "+ "TEST BAŞARISIZ! Giriş yapılamadı")
            self.driver.execute_script("window.history.go(-1)")
            self.driver.refresh()

    # Yanlış mail adresi girme testi.#
    def wrong_mail_login(self, username, password):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        try:
            x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[4]/div").text
            if x == "Customer not found.":
                print("wrong_mail_login --->   " + "TEST BAŞARILI! Giriş yapılamadı. " + "İstenilen hata mesajı alındı: " + x)
            elif x == "Kullanıcı adı ya da şifre hatalı.":
                print("wrong_mail_login --->  " + "TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")
            self.driver.refresh()
        except:
            print("wrong_mail_login --->   " + "TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")
            self.driver.refresh()

    #Yanlış şifre girme testi.#
    def wrong_password_login(self, username, password):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()

        try:
            x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[4]/div").text
            if  x == "Kullanıcı adı ya da şifre hatalı." :
                print("wrong_password_login --->  "+ "TEST BAŞARILI! Giriş yapılamadı. " + "İstenilen hata mesajı alındı: " + x)

            self.driver.execute_script("window.history.go(-1)")
            self.driver.refresh()
        except:
            print("wrong_password_login --->   "+"TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")
            self.driver.refresh()

    #Geçersiz mail girme testi.
    def invalid_login(self, username, password):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        try:
            x = self.driver.find_element(By.ID, "userName-helper-text").text

            if x == "Geçersiz e-posta adresi" :

                print("invalid_login --->   "+"TEST BAŞARILI! Giriş yapılamadı. "  + "İstenilen hata mesajı alındı: " + x)

            self.driver.execute_script("window.history.go(-1)")
            self.driver.refresh()
        except:
            print("invalid_login --->   " + "TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")
            self.driver.refresh()



