from time import sleep

from helpers.base_pytest import Base


class TestID0013(Base):
    """
        TestCase: 0013
        Author: Iryna Vaskiv
        Description:
            Check if "Новинки" button work correct.
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find correct button and click it
            3. Sleep few seconds
            4. Find new element in second page
        Expected result:
            1. Should be 1 element.
    """

    def test_new_button(self):
        self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/'
            'li[2]/a').click()
        sleep(5)
        all_novelty_header = self.all_novelty_header()
        assert len(all_novelty_header) == 1
