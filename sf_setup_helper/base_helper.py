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

    def teardown(self):
        self.selenium.close()
