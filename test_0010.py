from base_pytest import Base


class TestID0010(Base):
    """
        TestCase: 0010
        Author: Iryna Vaskiv
        Description: Check if "NEW" label exist in page.
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find correct xpath to label
        Expected result:
            1. Should be 1 element.
    """

    def test_if_exist_new_label(self):
        new_label = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[6]/span')
        if_exist_new_label = len(new_label)
        assert if_exist_new_label == 1
