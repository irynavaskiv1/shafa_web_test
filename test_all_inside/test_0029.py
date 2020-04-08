import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0029(Base):
    """
        @TestCase: 0029 (1)
        @Author: Iryna Vaskiv
        Description:
            1. Check if items inside main block have all fields.
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click shafa.ua site
            2. Select block items inside main page
            3. Get children ids
        Expected result:
            1. Children ids should have all correct items
    """

    def test_items_inside_mail_block(self):
        """ for vip-revelation"""
        html_list = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[4]/div/ul[1]')
        children_ids = html_list.find_elements_by_tag_name("li")
        only_price = [i for i in children_ids if 'грн' in i.text]
        result = (True if len(only_price) > 0 else False)
        result2 = [True for i in only_price if len(i.text) > 5]
        assert result == True
        assert all(result2) == True
