from base_pytest import Base


class TestID008(Base):

    def test_we_are_on_social_networks(self):
        all_social_network = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[3]/div[1]/footer/div/div/div/div/ul[3]')
        all = len(all_social_network)
        assert all == 1

    def test_numbers_of_cities(self):
        city_index = self.selenium.find_element_by_class_name(
            'b-index-about__cities')
        numbers_of_city = city_index.find_elements_by_tag_name('li')
        assert len(numbers_of_city) == 20

    def test_numbers_of_brands(self):
        brand_index = self.selenium.find_element_by_class_name(
            'b-brands')
        numbers_of_brands = brand_index.find_elements_by_tag_name('li')
        assert len(numbers_of_brands) == 18