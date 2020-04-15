import pytest

from sf_setup_helper.base_pytest import Base
from sf_setup_helper.base_helper import BaseHelper


@pytest.mark.webtest
class TestID0029(Base, BaseHelper):
    """
        @TestCase: 0029 (1, 2, 3, 4)
        @Author: Iryna Vaskiv
        Description:
            1. Check if items inside main block have all fields.
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click shafa.ua site
            2. Select block items inside main page
            3. Get children ids
        Expected result:
            1. Children ids should have all correct items
    """

    def test_items_inside_mail_block(self):
        """ for vip-revelation"""
        html_list = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[4]/div/ul[1]')
        result = self.iteration_by_items(html_list)
        result2 = [True for i in self.only_price if len(i.text) > 5]
        assert result == True
        assert all(result2) == True

    def test_items2_inside_mail_block(self):
        """ for vip-men"""
        html_list = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[4]/div/ul[2]')
        result = self.iteration_by_items(html_list)
        result2 = [True for i in self.only_price if len(i.text) > 5]
        assert result == True
        assert all(result2) == True

    def test_items3_inside_mail_block(self):
        """ for vip-children"""
        html_list = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[4]/div/ul[3]')
        result = self.iteration_by_items(html_list)
        result2 = [True for i in self.only_price if len(i.text) > 5]
        assert result == True
        assert all(result2) == True

    def test_items4_inside_mail_block(self):
        """ popular goods"""
        html_list = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[5]/div')
        result = self.iteration_by_items(html_list)
        result2 = [True for i in self.only_price if len(i.text) > 5]
        assert result == True
        assert all(result2) == True
