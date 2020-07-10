from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest


class BasePage(object):
    def __init__(self, browser_driver):
        self.driver = browser_driver
