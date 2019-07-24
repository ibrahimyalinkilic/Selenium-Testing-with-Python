from selenium import webdriver

class SignUp:

    def __init__(self,userName,name,surName,password,referrerCode):
        self.userName = userName
        self.name = name
        self.surName = surName
        self.password = password
        self.referrerCode = referrerCode

    def signup(self):

        driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[2]/span[1]").click()
        driver.find_element_by_id("userName").send_keys(self.userName)
        driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        driver.find_element_by_id("name").send_keys(self.name)
        driver.find_element_by_id("surname").send_keys(self.surName)
        driver.find_element_by_id("password").send_keys(self.password)
        driver.find_element_by_id("password2").send_keys(self.password)
        driver.find_element_by_id("referrerCode").send_keys(self.referrerCode)
        driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[8]/span/span[1]/input").click()
        driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()

    def check(self):
        xpath = "//*[@id='root']/div/div[3]/div[9]/div"
        if driver.find_element_by_xpath(xpath) == True:
            print(self.userName + "Adlı bir kullanıcı zaten var.")

        elif driver.find_element_by_xpath(xpath) == False:
            print("Kayıt Başarılı.")


driver = webdriver.Chrome()
url = "https://dev.bitexen.com/"
driver.get(url)
driver.maximize_window()


user1 = SignUp("something", "ibrahim", "yalinkilic", "asdsdaf23", " ")
user1.signup()