from sf_setup_helper.base_pytest import Base


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
