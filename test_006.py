from time import sleep
from base_pytest import Base


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
        sleep(5)

        self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div/div/div[2]/form/button')\
            .click()
