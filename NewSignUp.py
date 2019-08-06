from selenium import webdriver
from selenium.webdriver.common.by import By


class signup:

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.bitexen.com/")
        self.driver.implicitly_wait(5)

    # Tarayıcı kapama fonksiyonu
    def teardown(self):
        self.driver.quit()

    # Kayıtlı kullanıcı

    def already_registered_signup(self,username,name,surname,password,rePassword,referrenceCode):

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("surname").send_keys(surname)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("password2").send_keys(rePassword)
        self.driver.find_element_by_id("referrerCode").send_keys(referrenceCode)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        try:
            x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[9]/div").text
            if x == 'Kullanıcı zaten mevcut.':
                print("registered_signup --->  "+"TEST BAŞARILI! Üye olunamadı. " + "İstenilen hata mesajı alındı: " + x)
                self.driver.execute_script("window.history.go(-1)")

        except:
            print("registered_signup --->  "+"TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")

    # Geçersiz mail

    def invalid_mail_signup(self,username,name,surname,password,rePassword,referrenceCode):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("surname").send_keys(surname)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("password2").send_keys(rePassword)
        self.driver.find_element_by_id("referrerCode").send_keys(referrenceCode)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        try:
            x = self.driver.find_element(By.ID,"userName-helper-text").text
            if x == "Geçersiz e-posta adresi":
                print("invalid_mail_signup --->  "+"TEST BAŞARILI! Üye olunamadı. " + "İstenilen hata mesajı alındı: " + x)
                self.driver.execute_script("window.history.go(-1)")

        except:
            print("invalid_mail_signup --->  "+"TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")

    # Şifre alanı boş

    def password_is_empty_signup(self,username,name,surname,password,rePassword,referrenceCode):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("surname").send_keys(surname)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("password2").send_keys(rePassword)
        self.driver.find_element_by_id("referrerCode").send_keys(referrenceCode)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        try:
            x = self.driver.find_element(By.ID,"password-helper-text").text
            if x == "Boş bırakılamaz":
                print("empty_password_signup --->  "+"TEST BAŞARILI! Üye olunamadı. " + "İstenilen hata mesajı alındı: " + x)
                self.driver.execute_script("window.history.go(-1)")

        except:
            print("empty_password_signup --->  "+"TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")

    # Şifreler eşleşmiyor

    def passwords_doesnt_match_signup(self,username,name,surname,password,rePassword,referrenceCode):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("surname").send_keys(surname)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("password2").send_keys(rePassword)
        self.driver.find_element_by_id("referrerCode").send_keys(referrenceCode)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        try:
            x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[9]/div").text
            if x == "Girdiğiniz şifreler eşleşmiyor":
                print("wrong_password_signup --->  "+"TEST BAŞARILI! Üye olunamadı. " + "İstenilen hata mesajı alındı: " + x)
                self.driver.execute_script("window.history.go(-1)")

        except:
            print("wrong_password_signup --->  "+"TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")

    # Şifre yeterince uzunlukta değil

    def password_not_long_enough_signup(self,username,name,surname,password,rePassword,referrenceCode):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("surname").send_keys(surname)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("password2").send_keys(rePassword)
        self.driver.find_element_by_id("referrerCode").send_keys(referrenceCode)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        try:
            x = self.driver.find_element(By.XPATH, "//*[@id='password-helper-text']").text
            if x == "Şifreniz en az 8 karakter olmalıdır":
                print("password_not_long_enough_signup --->  "+"TEST BAŞARILI! Üye olunamadı. " + "İstenilen hata mesajı alındı: " + x)
                self.driver.execute_script("window.history.go(-1)")

        except:
            print("password_not_long_enough_signup --->  "+"TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")

    # Kullanıcı sözleşmesi onaylanmadı

    def unselected_checkbox(self,username,name,surname,password,rePassword,referrenceCode):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        self.driver.find_element_by_id("userName").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("surname").send_keys(surname)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("password2").send_keys(rePassword)
        self.driver.find_element_by_id("referrerCode").send_keys(referrenceCode)
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        try:
            x = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[9]/div").text
            if x == "Lütfen kullanıcı sözleşmesini onaylayınız":
                print("unselected_checkbox --->  "+"TEST BAŞARILI! Üye olunamadı. " + "İstenilen hata mesajı alındı: " + x)
                self.driver.execute_script("window.history.go(-1)")

        except:
            print("unselected_checkbox --->  "+"TEST BAŞARISIZ! İstenilen hata mesajı alınamadı.")
            self.driver.execute_script("window.history.go(-1)")
