import time


def test_regist_from_login(pages):
    main_page = pages.main_page
    main_page.login_link.click()
    time.sleep(3)
    main_page.registration_link.click()
    time.sleep(3)
    main_page.registration(
        name="Ksenia",
        email="ksenia_13@smartreading.ru",
        password="ksenia_13@smartreading.ru",
        password_confirm="ksenia_13@smartreading.ru"
    )
    time.sleep(3)
    main_page.login_link.click()
    assert main_page.days_7_subscription_in_personal_account.text == "7"
    time.sleep(3)


