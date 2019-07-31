from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time


class WebTable:

    def __init__(self, webtable):
        self.table = webtable

    def get_row_count(self):
        return len(self.table.find_elements_by_tag_name("tr"))

    def get_column_count(self):
        return len(self.table.find_elements_by_xpath("//tr[2]/td"))

    def get_table_size(self):
        return {"rows": self.get_row_count(),
                "columns": self.get_column_count()}

    def row_data(self, row_number):

        row_number = row_number + 1
        row = self.table.find_elements_by_xpath("//tr["+str(row_number)+"]/td")
        rData = []
        for webElement in row:
            rData.append(webElement.text)

        return rData

    def column_data(self, column_number):
        col = self.table.find_elements_by_xpath("//tr/td["+str(column_number)+"]")
        rData = []
        for webElement in col:
            rData.append(webElement.text)
        return rData

    def get_all_data(self):
        # get number of rows
        noOfRows = len(self.table.find_elements_by_xpath("//tr")) - 1
        # get number of columns
        noOfColumns = len(self.table.find_elements_by_xpath("//tr[2]/td"))
        allData = []
        # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in range(1, noOfRows):
            # reset the row data every time
            ro = []
            # iterate over columns
            for j in range(1, noOfColumns) :
                # get text from the i th row and j th column
                ro.append(self.table.find_element_by_xpath("//tr["+str(i)+"]/td["+str(j)+"]").text);

            # add the row data to allData of the self.table
            allData.append(ro)

        return allData

    def get_cell_data(self, row_number, column_number):
        if(row_number == 0):
            raise Exception("Row number starts from 1")

        row_number = row_number+1
        cellData = self.table.find_element_by_xpath("//tr["+str(row_number)+"]/td["+str(column_number)+"]").text
        return cellData


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://dev.bitexen.com/")
        self.driver.implicitly_wait(10)

    def test_web_table(self):

        self.driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[1]/div/div/div[2]/a[1]").click()
        self.driver.find_element_by_id("userName").send_keys("username@gmail.com")
        self.driver.find_element_by_id("password").send_keys("password")
        self.driver.find_element_by_xpath("//*[@id='root']/div/div[3]/button/span[1]").click()
        time.sleep(3)
        self.driver.get("https://dev.bitexen.com/account/assets")

        time.sleep(3)
        w = WebTable(self.driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div"))

        print("No of rows : ", w.get_row_count())
        print("------------------------------------")
        print("No of cols : ", w.get_column_count())
        print("------------------------------------")
        print("Table size : ", w.get_table_size())
        print("------------------------------------")
        print("First row data : ", w.row_data(0))
        print("------------------------------------")
        print("First column data : ", w.column_data(1))
        print("------------------------------------")
        print("All table data : ", w.get_all_data())
        print("------------------------------------")
        print("Get data from Cell : ", w.get_cell_data(2, 2))


if __name__ == "__main__":
    unittest.main()

