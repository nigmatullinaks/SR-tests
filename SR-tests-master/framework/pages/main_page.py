from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.rates_page import RatePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    @property
    def login_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "headAuth"))
        )
        return element



    @property
    def header_rates (self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"headBox")]'
                                                  '//a[contains(@href,"https://b2b.skiliks.com/rates")]'))
        )
        return element

    @property
    def author_email_input(self):
        return self.driver.find_element(By.NAME, 'email')

    @property
    def author_password_input(self):
        return self.driver.find_element(By.NAME, 'password')

    @property
    def author_enter_button(self):
        return self.driver.find_element(By.XPATH, '//form[@id="login-form"]//button[@type="submit"]')

    def login(self, email, password):
        self.author_email_input.send_keys(email)
        self.author_password_input.send_keys(password)
        self.author_enter_button.click()

    @property
    def registration_link(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="pupUp--tabItem"]'))
        )
        return element


    @property
    def registration_name_input(self):
        return self.driver.find_element(By.ID, 'regLogin')

    @property
    def registration_email_input(self):
        return self.driver.find_element(By.XPATH, '//input[@id="email"]')

    @property
    def registration_password_input(self):
        return self.driver.find_element(By.XPATH, '//input[@id="authPass"]')

    @property
    def registration_password_confirm_input(self):
        return self.driver.find_element(By.XPATH, '//input[@id="password-confirm"]')

    @property
    def registration_enter_button(self):
        return self.driver.find_element(By.XPATH, '//form[@id="registration-form"]//button[@type="submit"]')

    def registration(self, name, email, password, password_confirm):
        self.registration_name_input.send_keys(name)
        self.registration_email_input.send_keys(email)
        self.registration_password_input.send_keys(password)
        self.registration_password_confirm_input.send_keys(password_confirm)
        self.registration_enter_button.click()


    @property
    def days_subscription_in_personal_account(self):
        return self.driver.find_element(By.XPATH, '//div[@class="leftBlock"]//div[@class="subscribeTime"]')

    # @property
    # def days_7_subscription_in_personal_account(self):
    #     return self.driver.find_element(By.XPATH, '//div[@class="leftBlock"]//span[@class="subscribeTime--day"]')

    @property
    def days_7_subscription_in_personal_account(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="leftBlock"]//span[@class="subscribeTime--day"]'))
        )
        return element



    # @property
    # def thank_you_page(self):
    #     return self.driver.find_element(By.XPATH, '//div[@class="ratesStatus--title"]')
    #

    @property
    def thank_you_page(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="ratesStatus--title"]'))
        )
        return element

    @property
    def thank_you_page_gifts(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="ratesStatus--title"]'))
        )
        return element