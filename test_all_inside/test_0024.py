import random
import re
from time import sleep

import pytest

from sf_setup_helper.base_helper import BaseHelper


@pytest.mark.webtest
class TestID0024(BaseHelper):
    """
        @TestCase: 0024
        @Author: Iryna Vaskiv
        Description:
            1. Check if all blocks of items are visible
        Pre-condition: Login inside web/mobile interface.
        Steps to reproduce:
            1. Click in 'Search' button
            2. Enter the value to search block
            3. Check the value is shows correct
            4. Check the value inside boxes
        Expected result:
            1. Value in page should have all items
    """

    def test_block_inside(self):
        search_input = self.search_block()
        search_input.click()
        random_value = random.choice(
            ['Піджак', 'Жакет', 'Спідниця', 'Штани', 'Шорти'])
        search_input.send_keys(random_value)
        search_input.send_keys(u'\ue007')
        sleep(5)
        block_items = self.block_all_items_inside().text
        pattern = re.compile('TOP NEW')
        result = pattern.findall(block_items)
        is_label_exist = []
        if len(result) > 0:
            is_label_exist.append(True)
        assert is_label_exist[0]
