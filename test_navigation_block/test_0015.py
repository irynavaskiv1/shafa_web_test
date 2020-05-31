from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0015(Base):
    """
        TestCase: 0015(1, 2)
        Author: Iryna Vaskiv
        Description:
            1. Check if user can see all elements into Shafa.ua site.
             Should use 'Вся женская одежда' button inside 'Женщинам' block
            2. Check if brands have all elements(21)
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Женщинам' button
            2. Click in 'Вся женская одежда' button
            3. Check the header inside page
        Expected result:
            1. Should be 'Женская одежда' header.
            2. Should be 21 elements.
    """

    def test_all_women_site(self):
        self.for_women().click()
        self.all_woman_close().click()
        sleep(5)
        all_women_header = self.all_women_header()
        set_get_women_header = set(all_women_header.text.split('\n'))
        set_words = {'Женская одежда'}
        assert set_words == set_get_women_header

    def test_all_women_elements(self):
        self.for_women().click()
        self.all_woman_close().click()
        sleep(5)
        container_elements = self.container_elements()
        child_elements = container_elements. \
            find_elements_by_class_name('b-subcategories__item')
        if len(child_elements) != 21:
            pytest.skip(msg='Page do not have all elements')
        assert len(child_elements) == 21
