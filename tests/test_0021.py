import re
from time import sleep
import webcolors

import pytest

from helpers.base_pytest import Base


@pytest.mark.webtest
class TestID0021(Base):
    """
        @TestCase: 0021 (1, 2, 3 )
        @Author: Iryna Vaskiv
        Description:
            1. Check if user can see all items of color into Shafa.ua site.
             Should use 'Для дома' button.
            2. Check if first color (white) is actual white
            3. Check if all colors are correct.
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Для дома' button
            2. Check the section container inside page
            3. Check the all items inside 'Цвет' block
        Expected result:
            1. 'Для дома' should have section container block
            2. Container block should have white color
            3. Container block should have all correct colors
    """

    def test_len_color(self):
        self.for_home().click()
        self.all_home_textiles().click()
        elements = self.selenium.find_elements_by_class_name(
            'b-color-list__label')
        assert len(elements) == 24

    def test_white_color(self):
        self.for_home().click()
        self.all_home_textiles().click()
        sleep(1)
        element = self.selenium.find_element_by_class_name(
            'b-color-list__label')
        full_rgb = element.value_of_css_property('background-color')
        rgb_list = list(
            re.search(r'rgb\((\d+),\s*(\d+),\s*(\d+)', full_rgb).groups())
        rgb_clear = [int(i) for i in rgb_list]
        name_color = webcolors.rgb_to_name(rgb_clear)
        assert name_color == 'white'

    def test_check_all_colors(self):
        self.for_home().click()
        self.all_home_textiles().click()
        sleep(1)
        elements = self.selenium.find_elements_by_class_name(
            'b-filter__content b-color-list')
        for element in elements:
            full_rgb = element.value_of_css_property('background-color')
            rgb_list = list(
                re.search(r'rgb\((\d+),\s*(\d+),\s*(\d+)', full_rgb).groups())
            rgb_clear = [int(i) for i in rgb_list]
            name_color = webcolors.rgb_to_name(rgb_clear)
            assert type(name_color) == str
