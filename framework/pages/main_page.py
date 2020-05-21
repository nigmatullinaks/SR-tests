from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    @property
    def login_link(self):
        return self.driver.find_element(By.CLASS_NAME, "headAuth")
