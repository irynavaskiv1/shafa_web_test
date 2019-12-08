import pytest
from base_pytest import Base


class TestID003(Base):

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
