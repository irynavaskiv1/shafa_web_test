import random
from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0023(Base):
    """
        @TestCase: 0023
        @Author: Iryna Vaskiv
        Description:
            1. Check if search is visible
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click in 'Search' button
            2. Enter the value to search block
            3. Check the value is shows correct
        Expected result:
            1. Value in second page is the same
    """

    # def test_search_func(self):
    #     search_input = self.selenium.find_element_by_xpath(
    #         '/html/body/div/div[2]/div[1]/div/'
    #         'div[1]/nav/div/form/input')
    #     search_input.click()
    #     random_value = random.choice(
    #         ['Піджак', 'Жакет', 'Спідниця', 'Штани', 'Шорти'])
    #     search_input.send_keys(random_value)
    #     search_input.send_keys(u'\ue007')
    #     sleep(5)
    #     catalog_search_block = self.selenium.find_element_by_xpath(
    #         '/html/body/div/div[2]/div[2]/div/div'
    #         '/div/div/div[1]/form/div[1]/input')
    #     input_value_second = catalog_search_block.get_attribute("value")
    #     assert random_value == input_value_second

    def test_search_block_item(self):
        search_input = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/'
            'div[1]/nav/div/form/input')
        search_input.click()
        random_value = random.choice(
            ['Піджак', 'Жакет', 'Спідниця', 'Штани', 'Шорти'])
        search_input.send_keys(random_value)
        search_input.send_keys(u'\ue007')
        sleep(5)
        search_block_value = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div'
            '/div/div[4]/div[1]/div').text
        assert random_value == search_block_value
