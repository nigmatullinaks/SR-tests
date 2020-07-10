import time

from pages import main_page


def test_pay_gifts_12months(pages):
    main_page = pages.main_page
    gifts_page = pages.gifts_page
    time.sleep(3)
    gifts_page.input_gifts_form_as_guest(
        name = "ksenia+88@smartreading.ru",
        sender_email = "ksenia+88@smartreading.ru",
        addressee_email = "ksenia+88@smartreading.ru"
    )
    gifts_page.button_gifts_12m.click()
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