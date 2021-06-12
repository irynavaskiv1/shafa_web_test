import pytest

from helpers.base_pytest import Base


@pytest.mark.webtest
class TestID0027(Base):
    """
        @TestCase: 0027 (1, 2)
        @Author: Iryna Vaskiv
        Description:
            1. Check if items inside block have all elements. (Check if all
                children ids have name, price, like, size)
            2. Check if items inside block have 'грн' word.
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click in 'Discount' button
            2. Click select first element inside rubric listbox
            3. Made iteration inside block (check all items)
        Expected result:
            1. Value in page should have all items and have the same len
            2. All items have 'грн' word
    """

    def test_item_inside_block_first(self):
        self.discount_day().click()
        self.women_clothes().click()
        html_list = self.html_list()
        children_ids = html_list.find_elements_by_tag_name("li")
        is_children_ids_exist = [i.text for i in children_ids]
        assert len(is_children_ids_exist) > 0
        result_each_item = [True for i in is_children_ids_exist if len(i) > 0]
        assert all(result_each_item) is True

    def test_item_inside_block_second(self):
        self.discount_day().click()
        self.women_clothes().click()
        html_list = self.html_list()
        children_ids = html_list.find_elements_by_tag_name("li")
        is_uan_exist_in_each_item = \
            [True for i in children_ids if 'грн' in i.text]
        assert all(is_uan_exist_in_each_item) is True
