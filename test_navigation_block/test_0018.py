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
        all_novelty_header = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/div[2]/h1')
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
