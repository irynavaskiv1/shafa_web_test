import re
import pytest
from time import sleep

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
        self.selenium.find_element_by_id('cost-from').send_keys('100')
        sleep(5)
        self.selenium.find_element_by_id('cost-to').send_keys('200')
        sleep(5)
        price_block = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/'
            'div/ul/li[1]/div/div[2]/div[1]/div/span[1]')
        text_in_price_block = price_block[0].text
        temp = re.findall(r'\d+', text_in_price_block)
        res = list(map(int, temp))
        result = 100 <= res[0] <= 200
        assert result is True
