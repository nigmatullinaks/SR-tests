import time


def test_author_from_login(pages):
    main_page = pages.main_page
    main_page.login_link.click()
    main_page.login(
        email="ksenia_12@smartreading.ru",
        password="ksenia_12@smartreading.ru"
    )
    # time.sleep(3)
    # main_page.login_link.click()
    # assert main_page.days_7_subscription_in_personal_account.text == "6"
    # time.sleep(3)