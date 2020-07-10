
class Pages(object):
    def __init__(self, driver, url_manager):
        self.driver = driver
        self.url_manager = url_manager

    @property
    def main_page(self):
        self.url_manager.main()
        from pages.main_page import MainPage
        return MainPage(self.driver)

    @property
    def rates_page(self):
        self.url_manager.rate()
        from pages.rates_page import RatePage
        return RatePage(self.driver)

    @property
    def gifts_page(self):
        self.url_manager.gifts()
        from pages.gifts_page import PayGifts
        return PayGifts(self.driver)

    @property
    def summary_page(self):
        self.url_manager.summary()
        from pages.summary_page import SummaryPage
        return SummaryPage(self.driver)