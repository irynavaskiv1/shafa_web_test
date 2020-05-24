import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0026(Base):
    """
        @TestCase: 0026 (1, 2, 3)
        @Author: Iryna Vaskiv
        Description:
            1. Check if inside discount block all elements have umber
               of elements
            2. Check the len items inside main block
            3. Check children elements inside item
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click in 'Discount' button
            2. Click select first element inside rubric listbox
        Expected result:
            1. Value in page should have all items and have the same len
    """

    def test_rubric_inside_discount_day_block(self):
        self.discount_day().click()
        self.women_clothes().click()
        all_elements = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/div/div[2]'
            '/div[2]/div/div/div').text
        numbers = len(all_elements.split('\n'))
        assert numbers % 2 == 0

    def test_len_items_inside_main_block(self):
        self.discount_day().click()
        html_list = self.html_list()
        child_element = html_list.find_elements_by_tag_name('li')
        assert len(child_element) > 10

    def test_item_inside_main_block(self):
        self.discount_day().click()
        html_list = self.html_list()
        child_element = html_list.find_elements_by_tag_name('li')
        item_text = child_element[0].text
        text_inside_item = item_text.split('\n')
        assert len(text_inside_item) == 4
        uan = 'грн'
        assert uan in text_inside_item[1]
