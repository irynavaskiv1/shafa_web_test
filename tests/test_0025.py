from time import sleep

import pytest

from helpers.base_pytest import Base
from selenium.webdriver.support.ui import Select


@pytest.mark.webtest
class TestID0025(Base):
    """
        @TestCase: 0025
        @Author: Iryna Vaskiv
        Description:
            1. Check if filter block inside Discount block work correct.
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click in 'Discount' button
            2. Click "combobox items" button
        Expected result:
            1. Value in page should have all items and have the same len
    """

    def test_filter_inside_discount_day_block(self):
        self.discount_day().click()
        select = Select(self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/p/span/select'))
        select.select_by_index(3)
        sleep(4)
        get_combobox_text = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/p/span').text
        text_list = get_combobox_text.split('\n')
        set_words = ['по дате добавления', 'по популярности',
                     'от дорогих к дешевым', 'от дешевых к дорогим']
        assert len(text_list) == len(set_words)
