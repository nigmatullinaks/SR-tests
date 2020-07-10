class URLManager(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def main(self):
        self.driver.set_window_size(1900,1000)
        self.driver.get(self.url)

    def rate(self):
        self.driver.get(self.url + "/rates")

    def gifts(self):
        self.driver.get(self.url + "/gifts")

    def summary(self):
        self.driver.get(self.url + "/summary")