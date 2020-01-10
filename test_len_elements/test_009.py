from sf_setup_helper.base_pytest import Base


class TestID009(Base):
    """
        TestCase: 009
        Author: Iryna Vaskiv
        Description: Check if main page have Google Play and App Store buttons.
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find block with AGoogle Play and App Store buttons
            3. Check len of this buttons
        Expected result: Should be able 2 elements.
    """

    def test_mobile_apps(self):
        test_outerwear = self.selenium.find_element_by_class_name(
            'b-mobile-apps')
        numbers_test_outerwear = test_outerwear.find_elements_by_class_name(
            'b-mobile-apps__link')
        assert len(numbers_test_outerwear) == 2
