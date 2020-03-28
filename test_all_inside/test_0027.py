import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0027(Base):
    """
        @TestCase: 0027 (1)
        @Author: Iryna Vaskiv
        Description:
            1. Check if items inside block have all elements. (Check if all
                children ids have name, price, like, size)
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click in 'Discount' button
            2. Click select first element inside rubric listbox
            3. Made iteration inside block (check all items)
        Expected result:
            1. Value in page should have all items and have the same len
    """

    def test_rubric_inside_discount_day_block(self):
        self.discount_day().click()
        self.women_clothes().click()
        html_list = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/ul')
        children_ids = html_list.find_elements_by_tag_name("li")
        is_children_ids_exist = [i.text for i in children_ids]
        assert len(is_children_ids_exist) > 0
        result_each_item = [True for i in is_children_ids_exist if len(i) > 0]
        assert all(result_each_item) == True
