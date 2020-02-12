from time import sleep
import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0022(Base):
    
    def test_cost_from_labels(self):
        self.discount_day().click()
        self.selenium.find_element_by_id('cost-from').send_keys('100')
        self.selenium.find_element_by_id('cost-to').send_keys('200')
        sleep(5)
        main_block = self.selenium.find_elements_by_class_name('b-main__block')
        price_block = self.selenium.find_elements_by_class_name(
            'b-tile-item__price')
        result = []
        for i in price_block:
            if price_block >= 100:
                if price_block <= 200:
                    result.append(True)
            else:
                result.append(False)
        assert result[0] == True
