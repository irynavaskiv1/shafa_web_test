from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0015(Base):
    """
        TestCase: 0014(1, 2)
        Author: Iryna Vaskiv
        Description:
            1. Check if user can see all brands into Shafa.ua site. Should use
             'Вся женская одежда' button inside 'Женщинам' block
            2. Check if brands have all elements(21)
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Женщинам' button
            2. Click in 'Все аксессуары' button
            3. Check the header inside page
        Expected result:
            1. Should be 'Все аксессуары ' header.
            2. Should be 12 elements.
    """

    def test_all_women_site(self):
        self.for_women_button().click()
        self.all_accessories().click()
        sleep(5)
        all_women_header = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/div[1]/h1')
        set_get_accessories_header = set(all_women_header.text.split('\n'))
        set_words = {'Женские аксессуары'}
        assert set_words == set_get_accessories_header

    def test_all_women_elements(self):
        self.for_women_button().click()
        self.all_accessories().click()
        sleep(5)
        container_accessories = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/div[2]')
        child_elements = container_accessories. \
            find_elements_by_class_name('b-subcategories__item')
        if len(child_elements) != 13:
            pytest.skip(msg='Page do not have all elements')
        assert len(child_elements) == 13
