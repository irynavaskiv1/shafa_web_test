from time import sleep
from base_pytest import Base


class TestID005(Base):

    def test_add_new_ware(self):
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
            '/html/body/div[1]/div/div/div/div/div/div[2]/form/button') \
            .click()
        name_of_ware = self.selenium.find_element_by_xpath(
            '//*[@id="product-name"]')
        name_of_ware.send_keys('Плаття')

        state = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/form/div[3]/ul/'
            'li[2]/div/div/span[1]/div[1]').click()
        state.select_by_index(0)

        close_for_women = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/form/div[4]/div[2]/'
            'div[1]').click()

        other_close = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/form/div[5]/div[2]/'
            'ul/li[16]').click()

        color = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/form/div[6]/div[2]/'
            'ul/li[1]').click()

        payment_method = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/form/div[8]/div[2]/'
            'label[1]/div').click()
        input_price = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/form/div[8]/div[2]/'
            'label[1]/span[1]')
        input_price.send_keys('200')

        i_add_one_photo = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/form/div[9]/label').click()

        add_ware = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/form/div[9]/button').click()
        sleep(10)

        should_be = self.selenium.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/p[1]')
        exist = 'Ваше обьявление было добавлено'

        assert should_be == exist
