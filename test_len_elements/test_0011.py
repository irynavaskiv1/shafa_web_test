from sf_setup_helper.base_pytest import Base


class TestID0011(Base):
    """
        TestCase: 0011
        Author: Iryna Vaskiv
        Description:
        Check the quantity of elements inside "Sections on the site Shafa.ua"
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Login into Shafa.ua
            2. Find correct box of button/buttons
            3. Check child elements inside box
        Expected result:
            1. Should be 3 elements.
    """

    def test_sections_of_women_close(self):
        sections = self.selenium.find_element_by_class_name(
            'b-columns_type_enumerated')
        number_of_sections = sections.find_elements_by_tag_name('li')
        assert len(number_of_sections) == 3
