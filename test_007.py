from base_pytest import Base


class TestID007(Base):

    def test_android_play_market(self):
        self.selenium.find_element_by_xpath(
            '/html/body/div/div[3]/div[2]/div/a[1]/img').click()
        label = list(self.selenium.find_elements_by_xpath(
            '/html/body/div[1]/c-wiz[1]/div/div[1]/div[1]/div[2]/div/a/img'))
        assert len(label) == 1

    def test_ios_app_store(self):
        self.selenium.find_element_by_xpath(
            '/html/body/div/div[3]/div[2]/div/a[2]/img').click()
        button1 = list(self.selenium.find_elements_by_xpath(
            '//*[@id="ac-gn-firstfocus"]'))
        assert len(button1) == 1
