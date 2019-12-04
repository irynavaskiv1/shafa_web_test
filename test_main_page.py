import pytest
from selenium import webdriver
from time import sleep


class Test01:

    @pytest.fixture(autouse=True)
    def prepare(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get('{}'.format('https://shafa.ua/'))
        sleep(2)

    def test_mobile_menu_all_elements(self):
        login = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/header/div[2]/div/a[1]')
        login.click()
        sleep(3)
        page_elements = self.selenium.find_elements_by_xpath(
            '/html/body/div[1]/div/div/div/div/div/div[2]')
        if len(page_elements) == 0:
            pytest.skip(msg='Page do not have any elements')
        assert page_elements == 2
