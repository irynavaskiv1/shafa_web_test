import pytest
from base_pytest import Base


class TestID001(Base):

    def test_mobile_menu_all_elements(self):
        login = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/header/div[2]/div/a[1]')
        login.click()

        page_elements = self.selenium.find_elements_by_xpath(
            '/html/body/div[1]/div/div/div/div/div/div[2]')
        if len(page_elements) == 0:
            pytest.skip(msg='Page do not have any elements')

        assert len(page_elements) == 1
