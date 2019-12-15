from base_pytest import Base


class TestID008(Base):

    def test_we_are_on_social_networks(self):
        all_social_network = self.selenium.find_elements_by_xpath(
            '/html/body/div/div[3]/div[1]/footer/div/div/div/div/ul[3]')
        all = len(all_social_network)
        assert all == 1
