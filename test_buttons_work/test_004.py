from time import sleep
from sf_setup_helper.base_pytest import Base


class TestID004(Base):
    """
        TestCase: 004
        Author: Iryna Vaskiv
        Description: Check if search button work.
        Pre-condition: Login inside mobile interface.
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find search button
            3. Click on search button and enter "Пальто" word
            4. Next page should have "Пальто" word
        Expected result: The word which user entered in first page, should be in
        second.
    """

    def test_search_function(self):
        input_text_should_be = 'Пальто'
        self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[1]/nav/div/form/input')\
            .send_keys(input_text_should_be)
        self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[1]/nav/div/form/input')\
            .send_keys(u'\ue007')
        sleep(5)
        catalog_search_input = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[1]/'
            'form/div[1]/input')
        input_text_exist = catalog_search_input.get_attribute('value')
        sleep(5)
        assert input_text_should_be == input_text_exist
