import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0028(Base):

    def test_items_inside_mail_block(self):
        html_list = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[4]/div/ul[1]')
        children_ids = html_list.find_elements_by_tag_name("li")
        only_price = [i for i in children_ids if 'грн' in i.text]
        result = (True if len(only_price) > 0 else False)
        result2 = [True for i in only_price if len(i.text) > 5]
        assert result == True
        assert all(result2) == True
