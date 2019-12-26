from base_pytest import Base


class TestID009(Base):
    """
        TestCase: 008(first 1, 2)
        Author: Iryna Vaskiv
        Description:
            1. Check if page have social network field.
            2. Check if page have all numbers of cities.
            3. Check if page have all numbers of brand.
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find correct box of button/buttons
            3. Check child elements inside box
        Expected result:
                1. Should be 1 element.
                2. Should be 20 elements.
                3. Should b 18 elements.
    """

    def test_if_exist_new_label(self):
        new_label = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[6]/span')
        if_exist_new_label = len(new_label)
        assert if_exist_new_label == 1
