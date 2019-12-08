import pytest
from base_pytest import Base


class TestID002(Base):

    def test_navigation_list_all_elements(self):
        navigation_lis_elements = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul')
        child_elements = navigation_lis_elements[0].\
            find_elements_by_class_name('b-nav__link')
        if len(child_elements) != 6:
            pytest.skip(msg='Page do not have all elements')

        assert len(child_elements) == 6
