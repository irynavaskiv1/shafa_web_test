from base_pytest import Base


class TestID009(Base):

    def test_mobile_apps(self):
        test_outerwear = self.selenium.find_element_by_class_name(
            'b-mobile-apps')
        numbers_test_outerwear = test_outerwear.find_elements_by_class_name(
            'b-mobile-apps__link')
        assert len(numbers_test_outerwear) == 2
