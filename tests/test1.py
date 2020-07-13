from BookingPage import AddChild


def test_booking_child(browser):
    booking_main_page = AddChild(browser)
    booking_main_page.go_to_site()
    booking_main_page.click_on_list()
    booking_main_page.click_add_child()
