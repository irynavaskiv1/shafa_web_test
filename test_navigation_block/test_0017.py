from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0017(Base):
    """
        TestCase: 0017(1, 2)
        Author: Iryna Vaskiv
        Description:
            1. Check if user can see all cosmetic into Shafa.ua site.
             Should use 'Вся женская одежда' button inside 'Женщинам' block
            2. Check if brands have all elements
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Женщинам' button
            2. Click in 'Вся косметика' button
            3. Check the header inside page
        Expected result:
            1. Should be 'Женская косметика' header.
            2. Should be 7 elements.
    """

    def test_all_cosmetics(self):
        self.for_women().click()
        self.all_cosmetics().click()
        sleep(5)
        all_cosmetics_header = self.all_women_header()
        set_get_cosmetics_header = set(all_cosmetics_header.text.split('\n'))
        set_words = {'Женская косметика'}
        assert set_words == set_get_cosmetics_header

    def test_all_cosmetics_elements(self):
        self.for_women().click()
        self.all_cosmetics().click()
        sleep(5)
        container_cosmetics = self.selenium.find_element_by_xpath(
            '//*[@id="subcategories"]')
        child_elements = container_cosmetics. \
            find_elements_by_class_name('b-subcategories__item')
        if len(child_elements) != 7:
            pytest.skip(msg='Page do not have all elements')
        assert len(child_elements) == 7
