import pytest
from selenium import webdriver


class Base:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get('{}'.format('https://shafa.ua/'))

    def login_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/header/div[2]/div/a[1]')

    def signup_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/header/div[2]/div/a[2]')

    def add_ware(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/a')

    def for_women_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[1]/a')

    def all_woman_close(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]'
            '/nav/div/ul/li[1]/div/div[2]/div[1]/ul/li[1]/a')

    def all_brands(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]'
            '/nav/div/ul/li[1]/div/div[2]/div[1]/ul/li[2]/a')

    def novelty(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[2]/a')

    def for_kids(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[3]/a')

    def for_men(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[4]/a')

    def for_home(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[5]/a')

    def discount_day(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[6]/a')

    def teardown(self):
        self.selenium.close()
