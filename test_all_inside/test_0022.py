import re
import random
from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0022(Base):
    """
       @TestCase: 0022 (1)
       @Author: Iryna Vaskiv
       Description:
           1. Check if price block work correct. When user select price
           'from' and 'to' should select correct price.
       Pre-condition: Login inside web / mobile interface.
       Steps to reproduce:
           1. Click in 'Скидка дня' button
           2. Check the section containers inside page
           3. Check the all items inside 'Цена' container
       Expected result:
           1. For ex: should use price from 100 to 200 and check if all
           price in page are filter correct.
       """

    def test_cost_from_labels(self):
        self.discount_day().click()
        min_value = random.randint(100, 200)
        max_value = random.randint(200, 300)
        self.selenium.find_element_by_id('cost-from').send_keys(min_value)
        sleep(5)
        self.selenium.find_element_by_id('cost-to').send_keys(max_value)
        sleep(5)
        price_block = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/'
            'div/ul/li[1]/div/div[2]/div[1]/div/span[1]')
        text_in_price_block = price_block[0].text
        temp = re.findall(r'\d+', text_in_price_block)
        res = list(map(int, temp))
        result = min_value <= res[0] <= max_value
        assert result is True
