from sf_setup_helper.base_pytest import Base

import pytest


@pytest.mark.webtest
class TestID0020(Base):
    """
        @TestCase: 0020 (1, 2, 3 )
        @Author: Iryna Vaskiv
        Description:
            1. Check if user can see all items into Shafa.ua site.
             Should use 'Для дома' button.
            2. Check if user can see all items into Shafa.ua site.
             Should use 'Для дома' button.
            3. Check if price block have all items.
            (For ex:'От 300 до 500 грн', 'Более 1000 грн', 'До 100 грн',
                    'От 100 до 300 грн', 'От', 'Цена',  'До',)
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Для дома' button
            2. Check the section container inside page
            3. Check the all items inside 'Цена' block
        Expected result:
            1. 'Для дома' should have section container block
            2. Container block should have name of all items
            3. Container block should have name of all items
    """

    def test_if_first_main_inner_exist(self):
        self.for_home().click()
        self.all_home_textiles().click()
        all_item = self.all_item_inside_for_home()
        set_all_words = set(all_item.text.split('\n'))
        set_all_text = {'Shafa.ua', 'Для дома', 'Домашний текстиль'}
        assert set_all_words == set_all_text

    def test_if_second_main_inner_exist(self):
        self.for_home().click()
        self.all_home_textiles().click()
        all_item = self.all_item_inside_for_home()
        set_all_words = set(all_item.text.split('\n'))
        set_all_text = {'Посуда', 'Хранение вещей', 'Декор'}
        assert set_all_words == set_all_text

    def test_if_gradation_of_price_exist(self):
        self.for_home().click()
        self.all_home_textiles().click()
        all_city_words = self.all_city_words()
        set_all_words = set(all_city_words.text.split('\n'))
        set_all_text = {'От 300 до 500 грн', 'Более 1000 грн', 'До 100 грн',
                        'От 100 до 300 грн', 'От', 'Цена',  'До',
                        'От 500 до 1000 грн'}
        assert set_all_words == set_all_text
