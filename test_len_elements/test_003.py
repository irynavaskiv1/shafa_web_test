import pytest
from sf_setup_helper.base_pytest import Base


class TestID003(Base):
    """
       TestCase: 003
       Author: Iryna Vaskiv
       Description: Check if in "Woman" block have 4 sections.
       Pre-condition: Login inside web interface.
       Steps to reproduce:
           1. Login into Shafa.ua
           2. Find 'woman' button and click
           3. Check child elements
       Expected result: Should be 4 elements. If not skip test.
    """

    def test_navigation_list_all_elements(self):
        self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[1]/a')\
            .click()
        all_list = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[1]/div/'
            'div[1]')
        child_elements = all_list[0].\
            find_elements_by_class_name('b-sub-nav__section')
        if len(child_elements) != 4:
            pytest.skip(msg='Page do not have all elements')
        assert len(child_elements) == 4
