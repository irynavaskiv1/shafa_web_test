from time import sleep
from base_pytest import Base


class TestID0014(Base):
    """
        TestCase: 0014
        Author: Iryna Vaskiv
        Description: Check if user can see all brands into Shafa.ua site.
            Should use 'Все бренды' button inside 'Женщинам' block
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Женщинам' button
            2. Click in 'Все бренды' button
            3. Check the header inside page
        Expected result: Should be 'Брендовая женская одежда' header.
    """

    def test_logo_site(self):
        self.all_women_close_button().click()
        self.all_brands().click()
        sleep(5)
        brands_header = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/h1')
        set_get_brands_header = set(brands_header.text.split('\n'))
        set_words = {'Брендовая женская одежда'}
        assert set_words == set_get_brands_header
