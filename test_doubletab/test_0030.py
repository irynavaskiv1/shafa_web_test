import pytest

from time import sleep
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys


@pytest.mark.webtest
class TestID0030:
    """
        @TestCase: 0030 (1)
        @Author: Iryna Vaskiv
        Description:
            1. Check if new tab open when user click with "open in new tab".
               Also should check if inside second tab all elements are correct.
        Pre-condition: Login inside web interface.
        Steps to reproduce:
            1. Click shafa.ua site
            2. Select block item
            3. Click "open in new tab"
            4. Select second tab
            5. Check if all items inside second tab are correct
        Expected result:
            1. New tab should print correct information.
    """

    def test_if_possible_open_new_tab(self):
        browser = webdriver.Firefox()
        browser.get('{}'.format('https://shafa.ua/'))
        first_result = ui.WebDriverWait(browser, 15).until(
            lambda browser: browser.find_element_by_class_name('b-nav__link'))
        is_exist_elem_first_tab\
            = browser.find_element_by_class_name('b-nav__link')
        assert bool(is_exist_elem_first_tab) == True
        second_tab = first_result.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/nav/div/ul/li[7]/a')
        # Open the link in a new tab by sending key strokes on the element
        # Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN
        # to open tab on top of the stack
        second_tab.send_keys(Keys.CONTROL + Keys.RETURN)
        # Switch tab to the new tab, which we will assume
        # is the next one on the right
        browser.switch_to.window(browser.window_handles[-1])
        sleep(5)
        import ipdb; ipdb.set_trace()
        is_exist_elem_second_tab \
            = browser.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div/div/h1')
        assert bool(is_exist_elem_second_tab) == True
