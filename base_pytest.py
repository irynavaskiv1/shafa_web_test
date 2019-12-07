import pytest
from selenium import webdriver


class Base:

    @pytest.fixture(autouse=True)
    def prepare(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get('{}'.format('https://shafa.ua/'))

    def teardown(self):
        self.selenium.close()
