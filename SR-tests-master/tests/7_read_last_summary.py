import time


def test_read_last_summary(pages):
    main_page = pages.main_page
    main_page.login_link.click()
    main_page.login(
        email="ksenia+55@smartreading.ru",
        password="ksenia+55@smartreading.ru"
    )
    #time.sleep(3)
    summary_page = pages.summary_page
    #time.sleep(3)
    summary_page.summary_tab.click()
    time.sleep(3)
    summary_page.catalog_summary_scroll.click()
    time.sleep(3)





