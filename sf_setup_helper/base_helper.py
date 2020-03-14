import pytest
from selenium import webdriver


class BaseHelper:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get('{}'.format('https://shafa.ua/'))

    # items inside search block
    def search_block(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/form/input')

    def block_all_items_inside(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div[2]/div/ul[1]')

    def teardown(self):
        self.selenium.close()
