class URLManager(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def main(self):
        self.driver.get(self.url)

