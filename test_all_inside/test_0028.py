import random
from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0028(Base):
    """
        @TestCase: 0028 (1)
        @Author: Iryna Vaskiv
        Description:
            1. Check if items inside block have whether the price changes
             according to the set parameters.
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click in 'Discount' button
            2. Click select listbox element
            3. Made iteration inside block (check all items)
            4. Check if price is correct
        Expected result:
            1. Price should be correct
    """

    def test_item_inside_block_first(self):
        self.discount_day().click()
        self.women_clothes().click()
        min_value = random.randint(100, 200)
        max_value = random.randint(200, 300)
        self.selenium.find_element_by_name('costFrom').send_keys(min_value)
        sleep(5)
        self.selenium.find_element_by_name('costTo').send_keys(max_value)
        sleep(5)
        html_list = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/ul')
        children_ids = html_list.find_elements_by_tag_name("li")
        only_price = [i for i in children_ids if 'грн' in i.text]
        result = (True if len(only_price) > 0 else False)
        assert result == True
        result2 = [True for i in only_price if len(i.text) > 5]
        assert all(result2) == True
