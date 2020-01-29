from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0019(Base):
    """
        @TestCase: 0020
        @Author: Iryna Vaskiv
        Description:
            1. Check if user can see all items into Shafa.ua site.
             Should use 'Для дома' button.
            2. Check if user can see all items into Shafa.ua site.
             Should use 'Для дома' button.
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Для дома' button
            2. Check the section container inside page
        Expected result:
            1. 'Для дома' should have section container block
            2. Container block should have name of all items
    """

    def test_if_first_main_inner_exist(self):
        self.for_home().click()
        self.all_home_textiles().click()
        all_item = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/aside/div[1]/ul')
        set_all_words = set(all_item.text.split('\n'))
        set_all_text = {'Shafa.ua', 'Домашний текстиль', 'Для дома'}
        assert set_all_words == set_all_text

    def test_if_second_main_inner_exist(self):
        self.for_home().click()
        self.all_home_textiles().click()
        sleep(3)
        all_item = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/aside/div[1]/div')
        set_all_words = set(all_item.text.split('\n'))
        set_all_text = {'Посуда', 'Хранение вещей', 'Декор'}
        assert set_all_words == set_all_text
