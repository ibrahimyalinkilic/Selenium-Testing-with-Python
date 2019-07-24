from selenium import webdriver


class SignIn:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def signin(self):

        driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        print("Giriş yap butonuna basıldı.")
        driver.find_element_by_id("userName").send_keys(self.username)
        print("Mail adresiniz girildi. ")
        driver.find_element_by_id("password").send_keys(self.password)
        driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        print("Giriş yapılıyor...")


driver = webdriver.Chrome()

driver.maximize_window()

user1 = SignIn("something@gmail.com", "something")
user1.signin()