import random
from time import sleep
from selenium import webdriver

import pytest


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

    def search_function(self):
        """
        This function find search block in main page and input random value in
        search block.
        :return: None, just do some prepare actions.
        """
        search_input = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/'
            'div[1]/nav/div/form/input')
        search_input.click()
        self.random_value = random.choice(
            ['Піджак', 'Жакет', 'Спідниця', 'Штани', 'Шорти'])
        search_input.send_keys(self.random_value)
        search_input.send_keys(u'\ue007')
        sleep(5)

    def iteration_by_items(self, html_list):
        """
        This function made iteration by objects inside block.
        This function used in test_0029 .
        :param html_list: (list object)
        :return: result bool True/False (if True - len > 0 , else False)
        """
        self.children_ids = html_list.find_elements_by_tag_name("li")
        self.only_price = [i for i in self.children_ids if 'грн' in i.text]
        result = True if len(self.only_price) > 0 else False
        return result

    def login_discount_day_with_price_values(self):
        """
        This function made set values in two blocks.
        This function used in test_0028 .
        :param int
        :return: None
        """
        self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]'
            '/nav/div/ul/li[7]/a').click()
        self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/div/div[2]'
            '/div[2]/div/div/div/div[1]/div[1]/a').click()
        min_value = random.randint(100, 200)
        max_value = random.randint(200, 300)
        self.selenium.find_element_by_name('costFrom').send_keys(min_value)
        sleep(5)
        self.selenium.find_element_by_name('costTo').send_keys(max_value)
        sleep(5)

    def teardown(self):
        self.selenium.close()
