import pytest

from helpers.base_pytest import Base


@pytest.mark.webtest
class TestID0019(Base):
    """
        TestCase: 0019(1, 2)
        Author: Iryna Vaskiv
        Description:
            1. Check if user can see all items into Shafa.ua site.
             Should use 'Новинки' button inside 'Женщинам' block
            2. Check if brands have all elements
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click in 'Новинки' button
            2. Check the header inside page
        Expected result:
            1. 'Новинки' should have filter block with brands items
            2. Sorting block should have name of all items
            3. Sorting block should have all items
    """

    def test_if_brands_items_exist(self):
        self.novelty().click()
        size_block = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/aside/div/'
            'div/div[2]/div/div[5]/ul')
        set_get_size_block_words = set(size_block.text.split('\n'))
        set_words = {'George', 'Next', 'Atmosphere', 'New Look',
                     "Victoria's Secret", 'Италия', 'Mango', 'H&M',
                     'Бренд', 'Marks & Spencer', 'ZARA'}
        assert set_words == set_get_size_block_words

    def test_if_sorting_block_exist(self):
        self.novelty().click()
        self.size_block().click()
        set_get_size_block_words = set(self.size_block.text.split('\n'))
        set_words = {'по дате добавления', 'по популярности',
                     'от дорогих к дешевым', 'от дешевых к дорогим'}
        assert set_words == set_get_size_block_words

    def test_if_sorting_block_have_all_elements(self):
        self.novelty().click()
        self.size_block().click()
        set_get_size_block_words = set(self.size_block.text.split('\n'))
        set_words = {'по дате добавления', 'по популярности',
                     'от дорогих к дешевым', 'от дешевых к дорогим'}
        assert len(set_words) == len(set_get_size_block_words)
