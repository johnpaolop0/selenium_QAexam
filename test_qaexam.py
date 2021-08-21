from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class TestQAExam:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://qaexam.forge99.com/properties/")
        self.driver.maximize_window()

    def test_PriceDescending(self):
        element = self.driver.find_element(By.XPATH, "//select[@class='sort-sel aios-listings-sorter']")
        drop = Select(element)
        drop.select_by_visible_text('Price Descending')
        select_sort = self.driver.find_element(By.XPATH, "//select[@class='sort-sel aios-listings-sorter']/option[text()='Price Descending']").text
        assert select_sort == "Price Descending"

    def test_PriceAscending(self):
        element = self.driver.find_element(By.XPATH, "//select[@class='sort-sel aios-listings-sorter']")
        drop = Select(element)
        drop.select_by_visible_text('Price Ascending')    
        select_sort = self.driver.find_element(By.XPATH, "//select[@class='sort-sel aios-listings-sorter']/option[text()='Price Ascending']").text
        assert select_sort == "Price Ascending"

    def test_AZ(self):
        element = self.driver.find_element(By.XPATH, "//select[@class='sort-sel aios-listings-sorter']")
        drop = Select(element)
        drop.select_by_visible_text('A-Z') 
        select_sort = self.driver.find_element(By.XPATH, "//select[@class='sort-sel aios-listings-sorter']/option[text()='A-Z']").text
        assert select_sort == "A-Z"

    def test_ZA(self):
        element = self.driver.find_element(By.XPATH, "//select[@class='sort-sel aios-listings-sorter']")
        drop = Select(element)
        drop.select_by_visible_text('Z-A') 
        select_sort = self.driver.find_element(By.XPATH, "//select[@class='sort-sel aios-listings-sorter']/option[text()='Z-A']").text
        assert select_sort == "Z-A"    

    def test_clientWidth(self):
        self.driver.set_window_size(300, 300)
        print(self.driver.get_window_size())
        
    def teardown_method(self):
        self.driver.close()    


        

