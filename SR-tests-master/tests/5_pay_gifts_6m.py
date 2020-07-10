import time


def test_pay_gifts_6months(pages):
    main_page = pages.main_page
    main_page.login_link.click()
    main_page.login(
        email="ksenia+88@smartreading.ru",
        password="ksenia+88@smartreading.ru"
    )
    time.sleep(3)
    gifts_page = pages.gifts_page
    gifts_page.input_gifts_form(
        #name = "ksenia+88@smartreading.ru",
        #gifts_form = "ksenia+88@smartreading.ru",
        addressee_email = "ksenia+88@smartreading.ru"
    )
    gifts_page.button_gifts_6m.click()
    time.sleep(3)
    time.sleep(3)
    gifts_page.switch_to_frame_data_card()
    time.sleep(3)
    gifts_page.open_card_pay_popup.click()
    time.sleep(3)
    gifts_page.fill_card_data()
    time.sleep(3)
    gifts_page.switch_to_frame_confirm()
    gifts_page.fill_confirm_data()
    time.sleep(5)
    gifts_page.close_popup_for_ok()
    assert main_page.thank_you_page_gifts.text == "Благодарим за покупку!"
