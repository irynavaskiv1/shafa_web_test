import pytest
from base_pytest import Base


class TestID002(Base):
    """
        TestCase: 002
        Author: Iryna Vaskiv
        Description: Check if in navigation list exist 6 elements.
        Pre-condition: Login inside web interface
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find navigation list
            3. Check child elements inside list.
        Expected result: Should be 6 elements. If not skip test.
        """

    def test_navigation_list_all_elements(self):
        navigation_list_elements = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul')
        child_elements = navigation_list_elements[0].\
            find_elements_by_class_name('b-nav__link')
        if len(child_elements) != 6:
            pytest.skip(msg='Page do not have all elements')
        assert len(child_elements) == 6
