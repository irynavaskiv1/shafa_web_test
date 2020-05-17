from time import sleep

import pytest

from sf_setup_helper.base_pytest import Base


class TestID006(Base):
    """
        TestCase: 006
        Author: Iryna Vaskiv
        Description: Check if user can login into Shafa.ua site.
        Pre-condition: Have login and password.
        Steps to reproduce:
            1. Click in "login" button
            2. Enter login into login field
            3. Enter password into password field
            4. Press "I'm not a robot"
            5. Press "Войти" button
        Expected result: Should be able to login into a page.
    """

    @pytest.mark.skip
    def test_login(self):
        login_button = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/header/div[2]/div/a[1]')
        login_button.click()
        sleep(5)

        login_field = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div/div/div[2]/form/div[1]/input')
        login_field.send_keys('iryna_vaskiv')

        password_field = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div/div/div[2]/form/div[2]/input')
        password_field.send_keys('qqqqqq1!')

        i_am_not_a_robot_button = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div/div/div[2]/form/button').click()
        sleep(5)

        login_inside_login_button = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div/div/div[2]/form/button').click()
        sleep(5)

        profile_image = self.selenium.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div/div[1]/header/'
            'div[2]/div/div/img')
        len_profile_image = len(profile_image)

        assert len_profile_image == 1
