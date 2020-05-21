from selenium import webdriver
import pytest


def get_url_manager(browser_driver):
    from managers.url_manager import URLManager

    return URLManager(browser_driver, "https://smartreading.ru")

@pytest.fixture(scope="function", name="url_manager")
def url_manager_fixture(browser_driver):
    return get_url_manager(browser_driver)


@pytest.fixture(scope="function", name="browser_driver")
def get_driver():
    return webdriver.Chrome("/Users/eduardnigmatullin/chromedriver")


def get_pages(browser_driver, url_manager):
    from pages.pages import Pages
    return Pages(browser_driver, url_manager)

@pytest.fixture(scope="function", name="pages")
def pages_fixture(browser_driver, url_manager):
    return get_pages(browser_driver, url_manager)



# driver = get_driver()
#
#
# wait = WebDriverWait(driver, 10)
# driver.get("https://smartreading.ru/")
#
# time.sleep(1)
# driver.find_element(By.CLASS_NAME, "headAuth").click()
#
# first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
# print(first_result.get_attribute("textContent"))