from selenium import webdriver
from NewSignIn import login


class Trade(login):

    # bekleyen alış emirlerinden birincisinin seçilip emir girme tablosuna doğru bi şekilde gelmesi
    def sell_select_first(self):

        self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/a/img").click()

        first = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[1]")
        first.click()
        total_price = self.driver.find_element_by_id("total-amount").get_attribute("value")

        amount = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/span")
        volume = self.driver.find_element_by_id('volume').get_attribute('value')

        value = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[3]")
        price = self.driver.find_element_by_id('price').get_attribute('value')
        volume = float(volume)
        amount_order = amount.text
        amount_order = float(amount_order)

        if first.text == total_price and amount_order == volume and value.text == price:
            print(
                "sell_select_first ---> " + "TEST BAŞARILI! " + "Satma işlemi doğru bir şekilde emir tablosuna geldi. "+ "Fiyat= " + price + " " + "TRY" + " , " + "Miktar= " + str(
                    volume) + " " + "BTC" + " , " + "Toplam= " + total_price + " " + "TRY")
        else:
            print("sell_select_first ---> " + "TEST BAŞARISIZ!")

    # bekleyen alış emirlerinden ikincisinin seçilip emir girme tablosuna doğru bi şekilde gelmesi
    def sell_select_second(self):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/a/img").click()

        second_cell = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[2]/td[1]")
        second_cell.click()

        amount_order = self.driver.find_element_by_id('volume').get_attribute('value')
        amount_order = float(amount_order)
        price_order = self.driver.find_element_by_id('price').get_attribute('value')
        price_order = float(price_order)

        total_price_order = self.driver.find_element_by_id("total-amount").get_attribute("value")
        total_price_order = float(total_price_order)

        amount1 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/span").text

        value1 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[3]").text

        amount2 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[2]/td[2]/span").text

        value2 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[2]/td[3]").text

        value1 = float(value1)
        value2 = float(value2)
        amount1 = float(amount1)
        amount2 = float(amount2)

        total_price = (amount1 * value1) + (amount2 * value2)
        total_price = round(total_price, 2)
        total_amount = amount2 + amount1

        if total_price_order == total_price and total_amount == amount_order and price_order == value2:
            print("sell_select_second --->" + "TEST BAŞARILI! " + "Satma işlemi doğru bir şekilde emir tablosuna geldi. " + "Fiyat= " + str(
                price_order) + " " + "TRY" + " , " + "Miktar= " + str(
                amount_order) + " " + "BTC" + " , " + "Toplam= " + str(
                total_price_order) + " " + "TRY")

        else:
            print("başarısız")

    # bekleyen alış emirlerinden sonuncusunun seçilip emir girme tablosuna doğru bi şekilde gelmesi
    def sell_select_all(self):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/a/img").click()
        table = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table")
        rows = len(table.find_elements_by_tag_name("tr"))

        self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[" + str(
                rows - 1) + "]/td[1]").click()
        last = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[" + str(
                rows - 1) + "]/td[3]").text
        last = float(last)
        amount_order = self.driver.find_element_by_id('volume').get_attribute('value')
        amount_order = float(amount_order)
        value_order = self.driver.find_element_by_id('price').get_attribute('value')
        value_order = float(value_order)
        total_price_order = self.driver.find_element_by_id("total-amount").get_attribute("value")
        total_price_order = float(total_price_order)

        i = 0
        total_price = 0
        total_amount = 0
        while i < rows - 1:
            value = float(self.driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[" + str(
                    i + 1) + "]/td[3]").text)
            amount = float(self.driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[" + str(
                    i + 1) + "]/td[2]/span").text)

            total_amount += amount
            total_price += value * amount
            i += 1
        total_amount = round(total_amount, 3)
        amount_order = round(amount_order, 3)
        total_price = round(total_price, 2)
        total_price_order = round(total_price_order, 2)

        if total_amount == amount_order and last == value_order and total_price_order == total_price:
            print(
                "sell_select_all --->" + "TEST BAŞARILI! " + "Satma işlemi doğru bir şekilde emir tablosuna geldi. " + "Fiyat= " + str(
                    value_order) + " " + "TRY" + " , " + "Miktar= " + str(
                    amount_order) + " " + "BTC" + " , " + "Toplam= " + str(
                    total_price_order) + " " + "TRY")
        else:
            print("sell_select_all ---> " + "TEST BAŞARISIZ!")

    # bekleyen satış emirlerinden birincisinin seçilip emir girme tablosuna doğru bi şekilde gelmesi
    def buy_select_first(self):

        self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/a/img").click()

        first = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]")
        first.click()
        total_price = self.driver.find_element_by_id("total-amount").get_attribute("value")

        amount = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/span")
        volume = self.driver.find_element_by_id('volume').get_attribute('value')

        value = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]")
        price = self.driver.find_element_by_id('price').get_attribute('value')
        volume = float(volume)
        amount_order = amount.text
        amount_order = float(amount_order)

        if first.text == total_price and amount_order == volume and value.text == price:
            print(
                "buy_select_first ---> " + "TEST BAŞARILI! " + "Satın alma işlemi doğru bir şekilde emir tablosuna geldi. " + "Fiyat= " + price + " " + "TRY" + " , " + "Miktar= " + str(
                    volume) + " " + "BTC" + " , " + "Toplam= " + total_price + " " + "TRY")
        else:
            print("buy_select_first ---> " + "TEST BAŞARISIZ!")

    # bekleyen satış emirlerinden ikincisinin seçilip emir girme tablosuna doğru bi şekilde gelmesi
    def buy_select_second(self):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/a/img").click()

        second_cell = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]")
        second_cell.click()

        amount_order = self.driver.find_element_by_id('volume').get_attribute('value')
        amount_order = float(amount_order)
        price_order = self.driver.find_element_by_id('price').get_attribute('value')
        price_order = float(price_order)
        total_price_order = self.driver.find_element_by_id("total-amount").get_attribute("value")
        total_price_order = float(total_price_order)

        amount1 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/span").text

        value1 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]").text

        amount2 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/span").text

        value2 = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]").text

        value1 = float(value1)
        value2 = float(value2)
        amount1 = float(amount1)
        amount2 = float(amount2)

        total_price = (amount1 * value1) + (amount2 * value2)
        total_price = round(total_price, 2)
        total_amount = amount2 + amount1

        if total_price_order == total_price and total_amount == amount_order and price_order == value2:
            print("buy_select_second --->" + "TEST BAŞARILI! " + "Satın alma işlemi doğru bir şekilde emir tablosuna geldi. "  + "Fiyat= " + str(
                price_order) + " " + "TRY" + " , " + "Miktar= " + str(
                amount_order) + " " + "BTC" + " , " + "Toplam= " + str(
                total_price_order) + " " + "TRY")

        else:
            print("başarısız")

    # bekleyen satış emirlerinden sonuncusunun seçilip emir girme tablosuna doğru bi şekilde gelmesi
    def buy_select_all(self):
        self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/a/img").click()
        table = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/table")
        rows = len(table.find_elements_by_tag_name("tr"))

        self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[" + str(
                rows - 1) + "]/td[1]").click()
        last = self.driver.find_element_by_xpath(
            "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[" + str(
                rows - 1) + "]/td[1]").text
        last = float(last)
        amount_order = self.driver.find_element_by_id('volume').get_attribute('value')
        amount_order = float(amount_order)
        value_order = self.driver.find_element_by_id('price').get_attribute('value')
        value_order = float(value_order)
        total_price_order = self.driver.find_element_by_id("total-amount").get_attribute("value")
        total_price_order = float(total_price_order)

        i = 0
        total_price = 0
        total_amount = 0
        while i < rows - 1:
            value = float(self.driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[" + str(
                    i + 1) + "]/td[1]").text)
            amount = float(self.driver.find_element_by_xpath(
                "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[" + str(
                    i + 1) + "]/td[2]/span").text)

            total_amount += amount
            total_price += value * amount
            i += 1
        total_amount = round(total_amount, 3)
        amount_order = round(amount_order, 3)
        total_price = round(total_price, 2)
        total_price_order = round(total_price_order, 2)

        if total_amount == amount_order and last == value_order and total_price_order == total_price:
            print("buy_select_all --->" + "TEST BAŞARILI! " + "Satın alma işlemi doğru bir şekilde emir tablosuna geldi. "  + "Fiyat= " + str(
                value_order) + " " + "TRY" + " , " + "Miktar= " + str(
                amount_order) + " " + "BTC" + " , " + "Toplam= " + str(
                total_price_order) + " " + "TRY")
        else:
            print("buy_select_all ---> " + "TEST BAŞARISIZ!")


