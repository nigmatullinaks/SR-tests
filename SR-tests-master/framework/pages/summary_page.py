from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class SummaryPage(BasePage):

    @property
    def summary_tab(self):
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="headNav--link " and text()="Библиотека"]'))
        )
        return element

    @property
    def catalog_summary(self):
        return self.driver.find_element(By.XPATH, '//*[@id="smooth"]/div[1]/div')

    @property
    def first_summary(self):
        return self.driver.find_element(By.XPATH, '//div[@class="productItem--imageBgcenter"][1] ')

    def catalog_summary_scroll(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.catalog_summary)
        self.first_summary.click()




