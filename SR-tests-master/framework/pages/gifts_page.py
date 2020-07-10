from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PayGifts(BasePage):


    @property
    def gifts_form(self):
        return self.driver.find_element(By.XPATH, '//form[@action="#"]')

    @property
    def input_sender_name(self):
        return self.driver.find_element(By.XPATH, '//input[@class="form--input" and @type="email"]')

    @property
    def input_sender_email(self):
        return self.driver.find_element(By.XPATH, '//input[@class="form--input" and @type="text"]')

    @property
    def input_addressee_email(self):
        return self.driver.find_element(By.XPATH, '//input[@type="email" and @placeholder="Укажите электронную почту получателя подарка"]')

    def input_gifts_form(self, addressee_email):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.gifts_form)
        self.input_addressee_email.send_keys(addressee_email)

    def input_gifts_form_as_guest(self, name, sender_email, addressee_email):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.gifts_form)
        self.input_sender_name.send_keys(name)
        self.input_sender_email.send_keys(sender_email)
        self.input_addressee_email.send_keys(addressee_email)

    @property
    def button_gifts_6m(self):
        return self.driver.find_element(By.XPATH, '//*[@id="gift-form-container"]/div[1]/div/div/div/div[1]/div[2]/button')

    @property
    def button_gifts_12m(self):
        return self.driver.find_element(By.XPATH,
                                        '//*[@id="gift-form-container"]/div[1]/div/div/div/div[2]/div[2]/button')

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
        return self.driver.find_element(By.XPATH, '//div[@class="widget-item-footer"]//button[@type="submit"]')

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