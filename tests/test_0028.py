import pytest

from helpers.base_pytest import Base
from helpers.base_helper import BaseHelper


@pytest.mark.webtest
class TestID0028(Base, BaseHelper):
    """
        @TestCase: 0028 (1, 2)
        @Author: Iryna Vaskiv
        Description:
            1. Check if items inside block have whether the price changes
             according to the set parameters.
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click in 'Discount' button
            2. Click select listbox element
            3. Made iteration inside block (check all items)
            4.2.1 Check if elements have reserved items
            4.2.2 Check if elements have new items
        Expected result:
            2.1. Reserved item should be in html list
            2.2 New item should be in html list
    """

    def test_item_inside_block_first(self):
        self.login_discount_day_with_price_values()
        html_list = self.html_list()
        children_ids = html_list.find_elements_by_tag_name("li")
        only_price = [i for i in children_ids if 'грн' in i.text]
        result = (True if len(only_price) > 0 else False)
        result2 = [True for i in only_price if len(i.text) > 5]
        assert result is True
        assert all(result2) is True

    def test_items_inside_events(self):
        self.login_discount_day_with_price_values()
        html_list = self.html_list().text()
        list_elements = html_list.split('\n')
        reserved = [i for i in list_elements if i == 'РЕЗЕРВ']
        is_reserved_elements_exist = True if len(reserved) > 0 else False
        new = [i for i in list_elements if i == 'NEW']
        is_new_elements_exist = True if len(new) > 0 else False
        assert is_reserved_elements_exist is True
        assert is_new_elements_exist is True
