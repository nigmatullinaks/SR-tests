
class Pages(object):
    def __init__(self, driver, url_manager):
        self.driver = driver
        self.url_manager = url_manager

    @property
    def main_page(self):
        self.url_manager.main()

        from pages.main_page import MainPage

        return MainPage(self.driver)

