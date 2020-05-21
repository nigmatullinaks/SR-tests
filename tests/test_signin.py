import time


def test_login(pages):
    main_page = pages.main_page
    main_page.login_link.click()
    # time.sleep(10)

