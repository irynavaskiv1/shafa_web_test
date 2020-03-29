import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0028(Base):
    """
        @TestCase: 0028 (1)
        @Author: Iryna Vaskiv
        Description:
            1. Check if items inside block have whether the price changes
             according to the set parameters.
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click in 'Discount' button
            2. Click select listbox element
            3. Made iteration inside block (check all items)
            4. Check if price is correct
        Expected result:
            1. Price should be correct
    """

    def test_item_inside_block_first(self):
        self.discount_day().click()
        self.women_clothes().click()
        import ipdb; ipdb.set_trace()
        self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/p/span/select')