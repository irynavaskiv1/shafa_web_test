from time import sleep

from base_pytest import Base


class TestID0012(Base):
    """
        TestCase: 0012
        Author: Iryna Vaskiv
        Description:
            Check if "Скидка дня" button work correct.
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find correct button and click it
            3. Sleep few seconds
            4. Find new element in second page
        Expected result:
            1. Should be 1 element.
    """

    def test_day_discount_button(self):
        self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/'
            'li[6]/a').click()
        sleep(5)
        day_discount_header = self.selenium.find_elements_by_class_name(
            'b-title')
        assert len(day_discount_header) == 1
