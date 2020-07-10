from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RatePage(BasePage):
    @property
    def input_promocode(self):
        return self.driver.find_element(By.XPATH, '//input[contains(@id,"promoCode")]')

    @property
    def button_apply_promocode(self):
        return self.driver.find_element_by_xpath('//span[text()="Применить промокод"]')

    @property
    def rate_6_month(self):
        return self.driver.find_element_by_xpath(
            '//div[@class="subscribe-plan__holder"]//img[contains(@src,"6-month@1x")]')

    @property
    def rate_12_month(self):
        return self.driver.find_element_by_xpath(
            '//div[@class="subscribe-plan__holder"]//img[contains(@src,"12-month@1x")]')


    @property
    def rate_18_month(self):
        return self.driver.find_element_by_xpath(
            '//div[@class="subscribe-plan__holder"]//img[contains(@src,"18-month@1x")]')



    @property
    def pay_card_button(self):
        return self.driver.find_element(By.ID, 'paymentMethodsContainer')

    @property
    def card_number_input(self):
        return self.driver.find_element(By.ID, 'cardNumber')

    @property
    def month_input(self):
        return self.driver.find_element(By.ID, 'inputMonth')

    @property
    def year_input(self):
        return self.driver.find_element(By.ID, 'inputYear')

    @property
    def cvc_input(self):
        return self.driver.find_element(By.ID, 'cardCvv')

    @property
    def confirm_input(self):
        return self.driver.find_element(By.XPATH, '//input[@id="password" and @type="tel"]')

    @property
    def open_card_pay_popup(self):
        return self.driver.find_element(By.XPATH, '//*[@id="paymentMethodsContainer"]/div[1]/button')

    @property
    def pay_button_in_popup(self):
        return self.driver.find_element (By.XPATH, '//div[@class="widget-item-footer"]//button[@type="submit"]')

    def switch_to_frame_data_card(self):
        frame_element = self.driver.find_element(By.XPATH, '//*[contains(@src,"payforms")]')
        return self.driver.switch_to.frame(frame_element)

    def switch_to_frame_confirm(self):
        frame_element = self.driver.find_element(By.XPATH, '//iframe[@class="default"]')
        return self.driver.switch_to.frame(frame_element)

    def switch_to_frame_ok(self):
        frame_element = self.driver.find_element(By.XPATH, '//*[@id="cp-scrollable-68111266"]/iframe')
        return self.driver.switch_to.frame(frame_element)

    def fill_card_data(self, card_number="4242424242424242", month="12", year="22", cvc="222"):
        self.card_number_input.send_keys(card_number)
        self.month_input.send_keys(month)
        self.year_input.send_keys(year)
        self.cvc_input.send_keys(cvc)
        self.pay_button_in_popup.click()

    @property
    def confirm_button_in_popup(self):
        return self.driver.find_element(By.XPATH, '//div[@class="text-center"]//button[@type="submit"]')


    def fill_confirm_data(self, two_plus_two="4"):
        self.confirm_input.send_keys(two_plus_two)
        self.confirm_button_in_popup.click()
        self.driver.switch_to.default_content()

    @property
    def ok_button_in_popup(self):
        frame_element = self.driver.find_element(By.XPATH, '//iframe[@class=" with-appled"]')
        self.driver.switch_to.frame(frame_element)
        return self.driver.find_element(By.XPATH, '//button[@class="btn btn-bor"]')

    def close_popup_for_ok(self):
        self.ok_button_in_popup.click()

