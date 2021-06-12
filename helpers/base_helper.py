import random

from time import sleep
from selenium import webdriver


selenium = webdriver.Firefox()


class BaseHelper:

    def __init__(self, random_value, children_ids, only_price):
        self.random_value = random_value
        self.children_ids = children_ids
        self.only_price = only_price

    def search_function(self):
        """
        This procedure find search block at the main page and input random value in search block.
        :return: None
        """
        search_input = selenium.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[1]/nav/div/form/input')
        search_input.click()
        self.random_value = random.choice(['Піджак', 'Жакет', 'Спідниця', 'Штани', 'Шорти'])
        search_input.send_keys(self.random_value)
        search_input.send_keys(u'\ue007')
        sleep(5)

    def iteration_by_items(self, html_list):
        """
        This function made iteration by objects inside block.
        This function used in test_0029 .
        :param html_list: (list object)
        :return: bool
        """
        self.children_ids = html_list.find_elements_by_tag_name("li")
        self.only_price = [i for i in self.children_ids if 'грн' in i.text]
        result = True if len(self.only_price) > 0 else False
        return result

    def login_discount_day_with_price_values(self):
        """
        This procedure made set values in two blocks.
        This procedure used in test_0028 .
        :param integer
        :return: None
        """
        selenium.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[7]/a').click()
        selenium.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/aside/div/div[2]/div[2]/div/div/div/'
                                       'div[1]/div[1]/a').click()
        min_value = random.randint(100, 200)
        max_value = random.randint(200, 300)
        selenium.find_element_by_name('costFrom').send_keys(min_value)
        sleep(5)
        selenium.find_element_by_name('costTo').send_keys(max_value)
        sleep(5)
