import time


def test_pay_12_months(pages):
    main_page = pages.main_page
    main_page.login_link.click()
    main_page.login(
        email="ksenia+88@smartreading.ru",
        password="ksenia+88@smartreading.ru"
    )
    time.sleep(3)
    rates_page = pages.rates_page
    rates_page.rate_12_month.click()
    time.sleep(5)
    rates_page.switch_to_frame_data_card()
    rates_page.open_card_pay_popup.click()
    rates_page.fill_card_data()
    time.sleep(3)
    rates_page.switch_to_frame_confirm()
    rates_page.fill_confirm_data()
    time.sleep(5)
    rates_page.close_popup_for_ok()
    assert main_page.thank_you_page.text == "Благодарим за подписку!"