from time import sleep
from base_pytest import Base


class TestID004(Base):
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
