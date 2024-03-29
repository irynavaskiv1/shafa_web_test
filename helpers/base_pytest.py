import pytest

from selenium import webdriver


class Base:

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.get('{}'.format('https://shafa.ua/'))

    # all header items
    def login_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/header/div[2]/div/a[1]')

    def signup_button(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/header/div[2]/div/a[2]')

    def search_input(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/'
            'div[1]/nav/div/form/input')

    def add_ware(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/a')

    def navigation_list_elements(self):
        return self.selenium.find_elements_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul')

    # items inside search block
    def search_block(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/form/input')

    def block_all_items_inside(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div[2]/div/ul[1]')

    # section container for 'Женщинам' button
    def for_women(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[1]/a')

    def all_woman_close(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]'
            '/nav/div/ul/li[1]/div/div[2]/div[1]/ul/li[1]/a')

    def all_brands(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]'
            '/nav/div/ul/li[1]/div/div[2]/div[1]/ul/li[2]/a')

    def all_accessories(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]'
            '/nav/div/ul/li[1]/div/div[2]/div[3]/ul/li/a')

    def all_cosmetics(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]'
            '/nav/div/ul/li[1]/div/div[2]/div[4]/ul/li/a')

    # section container for 'Новинки' button
    def novelty(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[2]/a')

    def all_novelty_header(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/div[2]/h1')

    def sorting_block(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div/div/div/'
            'div[4]/div[2]/span/select')

    def size_block(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div/div'
            '/div/div[4]/div[2]/span')

    # section container for 'Детям' button
    def for_kids(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[3]/a')

    def all_girls_clothes(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[3]'
            '/div/div[2]/div[1]/ul/li[1]/a')

    def all_baby_clothes(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[3]'
            '/div/div[2]/div[1]/ul/li[2]/a')

    def all_boys_clothes(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[3]'
            '/div/div[2]/div[2]/ul/li/a')

    def all_the_clothes_for_the_kids(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[3]'
            '/div/div[2]/div[3]/ul/li/a')

    # section container for 'Мужчинам' button
    def for_men(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[4]/a')

    def all_men_clothing(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[4]'
            '/div/div[2]/div[1]/ul/li/a')

    def all_men_shoes(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[4]'
            '/div/div[2]/div[2]/ul/li/a')

    def all_men_accessories(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[4]'
            '/div/div[2]/div[3]/ul/li/a')

    # section container for 'Для дома' button
    def for_home(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[5]/a')

    def all_home_textiles(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[1]/nav/div/ul/li[5]'
            '/div/div[2]/div[1]/ul/li[1]/a')

    def all_item_inside_for_home(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/aside/div[1]/div')

    def all_city_words(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/aside/div[2]'
            '/div[2]/div/div[1]')

    def all_utensils(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[5]'
            '/div/div[2]/div[2]/ul/li/a')

    def all_for_storing_things(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[5]'
            '/div/div[2]/div[3]/ul/li/a')

    def all_the_decor(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[5]'
            '/div/div[2]/div[4]/ul/li/a')

    def everything_for_home(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[5]'
            '/div/div[2]/div[1]/ul/li[2]/a')

    # section container for 'Скидка дня' button
    def discount_day(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[7]/a')

    def combobox_items_block(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/p/span/select')

    def html_list(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/ul')

    # section container for 'Рубрика' button
    def women_clothes(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/div/div[2]'
            '/div[2]/div/div/div/div[1]/div[1]/a')

    def children_clothes(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/div/div[2]'
            '/div[2]/div/div/div/div[2]/div[1]/a')

    def men_clothes(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/div/div[2]'
            '/div[2]/div/div/div/div[3]/div[1]/a')

    def for_home_stuff(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/div/div[2]'
            '/div[2]/div/div/div/div[4]/div[1]/a')

    def price_to_100(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/'
            'div/div[2]/div[3]/div/div[2]/div/ul/li[1]/label')

    def price_from_100_to_300(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/'
            'div/div[2]/div[3]/div/div[2]/div/ul/li[2]/label')

    def price_from_300_to_500(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/'
            'div/div[2]/div[3]/div/div[2]/div/ul/li[3]/label')

    def price_from_500_to_1000(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/'
            'div/div[2]/div[3]/div/div[2]/div/ul/li[4]/label')

    def price_from_1000(self):
        return self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/aside/'
            'div/div[2]/div[3]/div/div[2]/div/ul/li[5]/label')

    def teardown(self):
        self.selenium.close()
