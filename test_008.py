from base_pytest import Base


class TestID008(Base):
    """
        TestCase: 008(first)
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

    def test_we_are_on_social_networks(self):
        all_social_network = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[3]/div[1]/footer/div/div/div/div/ul[3]')
        all = len(all_social_network)
        assert all == 1

    def test_numbers_of_cities(self):
        city_index = self.selenium.find_element_by_class_name(
            'b-index-about__cities')
        numbers_of_cities = city_index.find_elements_by_tag_name('li')
        assert len(numbers_of_cities) == 20

    def test_numbers_of_brands(self):
        brand_index = self.selenium.find_element_by_class_name(
            'b-brands')
        numbers_of_brands = brand_index.find_elements_by_tag_name('li')
        assert len(numbers_of_brands) == 18


class TestID0081(Base):
    """
        TestCase: 008(second)
        Author: Iryna Vaskiv
        Description:
            1. Check if outerwear block has all elements.
            2. Check if skirt block has all elements.
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find correct box of button/buttons
            3. Check child elements inside box
        Expected result:
            1. Should be 9 element.
            2. Should be 9 elements.
    """

    def test_outerwear(self):
        test_outerwear = self.selenium.find_element_by_class_name(
            'b-index-categories__list')
        numbers_test_outerwear = test_outerwear.find_elements_by_tag_name('li')
        assert len(numbers_test_outerwear) == 9

    def test_skirt(self):
        test_skirt = self.selenium.find_element_by_class_name(
            'b-index-categories__list')
        numbers_test_skirt = test_skirt.find_elements_by_tag_name('li')
        assert len(numbers_test_skirt) == 9
