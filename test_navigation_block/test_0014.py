from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


class TestID0014(Base):
    """
        TestCase: 0014(1, 2)
        Author: Iryna Vaskiv
        Description:
            1. Check if user can see all brands into Shafa.ua site. Should use
             'Все бренды' button inside 'Женщинам' block
            2. Check if brands have all elements(16)
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Женщинам' button
            2. Click in 'Все бренды' button
            3. Check the header inside page
        Expected result:
            1. Should be 'Брендовая женская одежда' header.
            2. Should be 16 elements
    """

    def test_brands_site(self):
        self.for_women().click()
        self.all_brands().click()
        sleep(5)
        brands_header = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/h1')
        set_get_brands_header = set(brands_header.text.split('\n'))
        set_words = {'Брендовая женская одежда'}
        assert set_words == set_get_brands_header

    def test_all_brands(self):
        self.for_women().click()
        self.all_brands().click()
        sleep(5)
        container_brands = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div[2]/div[1]/div')
        child_elements = container_brands. \
            find_elements_by_class_name('b-brands__item_small')
        if len(child_elements) != 16:
            pytest.skip(msg='Page do not have all elements')
        assert len(child_elements) == 16
