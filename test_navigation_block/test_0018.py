import re
from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0018(Base):
    """
        TestCase: 0018(1, 2)
        Author: Iryna Vaskiv
        Description:
            1. Check if user can see all items into Shafa.ua site.
             Should use 'Новинки' button inside 'Женщинам' block
            2. Check if brands have all elements
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Новинки' button
            2. Check the header inside page
        Expected result:
            1. Should be 'Новинки: женская одежда' header.
            2. Should be 27 elements inside child elements.
    """
    def test_is_novelty_header_exist(self):
        self.novelty().click()
        sleep(5)
        all_novelty_header = self.all_novelty_header()
        set_get_novelty_header = set(all_novelty_header.text.split('\n'))
        set_words = {'Новинки: женская одежда'}
        assert set_words == set_get_novelty_header

    def test_get_all_child_elements(self):
        self.novelty().click()
        container_items = self.selenium.find_element_by_xpath(
            '//*[@id="subcategories"]')
        child_elements = container_items. \
            find_elements_by_class_name('b-subcategories__item')
        if len(child_elements) != 20:
            pytest.skip(msg='Page do not have all elements')
        assert len(child_elements) == 20

    def test_if_numbers_in_item_exist(self):
        self.novelty().click()
        item_all = self.all_novelty_item()
        item_text_number = re.findall('(\d+)', item_all.text)
        item_part = self.all_novelty_item_part()
        numbers = re.findall('(\d+)', item_part.text)
        assert int(item_text_number[0]) == int(numbers[0])

    def test_if_exist_size_filter(self):
        self.novelty().click()
        size_block = self.all_novelty_item_part()
        set_get_size_block_words = set(size_block.text.split('\n'))
        set_words = {'Другой', '50/5XL', '54/7XL', '40/L', '46/3XL', '44/XXL',
                     '38/M', '48/4XL', 'One size', '32/XXS', '52/6XL', '42/XL',
                     '36/S', '34/XS'}
        assert set_words == set_get_size_block_words
