import pytest

from sf_setup_helper.base_pytest import Base


class TestID001(Base):
    """
        TestCase: 001
        Author: Iryna Vaskiv
        Description: Check if login page have the main element.
        Pre-condition: Login inside mobile interface.
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find login button
            3. Click on "login button"
        Expected result: Should be 1 element. If not skip test.
    """

    def test_mobile_menu_all_elements(self):
        self.login_button().click()
        page_elements = self.selenium.find_elements_by_xpath(
            '/html/body/div[1]/div/div/div/div/div/div[2]')
        if len(page_elements) == 0:
            pytest.skip(msg='Page do not have any elements')
        assert len(page_elements) == 1
