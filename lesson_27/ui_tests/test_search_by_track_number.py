from lesson_27.UI.novaposhta.tracking_page import TrackingPage
import allure
tracking_number = '20450952733334'


@allure.feature("Search by track number")
def test_search_by_track_number(driver):
    tracking_page = TrackingPage(driver).open_page()

    assert tracking_page.current_page_url() == TrackingPage(driver).url

    tracking_page.fill_input_field(tracking_number).click_search_button()
    get_status = tracking_page.click_agree_button().get_status()

    assert get_status == "Отримана"
