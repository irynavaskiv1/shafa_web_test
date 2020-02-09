import pytest

from sf_setup_helper.base_pytest import Base


@pytest.mark.webtest
class TestID0020(Base):
    def test_cost_from_labels(self):
        self.discount_day().click()
        self.selenium.find_elements_by_id('cost-from').keys('100')
        self.selenium.find_elements_by_id('cost-to').keys('200')
        main_block = self.selenium.find_elements_by_class_name('b-main__block')
        price_block = self.selenium.find_elements_by_class_name(
            'b-tile-item__price')
        result = []
        for price_block in main_block:
            if price_block >= 100  and price_block <= 200:
                result.append(True)
            else:
                result.append(False)

        assert result[0] == True

