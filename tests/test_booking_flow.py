import logging
from pages.login_page import LoginPage
from pages.search_page import SearchFlightPage
from pages.result_page import ResultPage
from pages.booking_page import BookingPage
from pages.payment_page import PaymentPage
from utils.config import Config

logging.basicConfig(level=logging.INFO) 

def test_booking_flow(driver):
    logging.info("Launching application.")
    driver.get(Config.BASE_URL)

    logging.info("Logging in to application.")
    LoginPage(driver).login(Config.EMAIL, Config.PASSWORD)

    logging.info("Searching flights from MAA to LHR.")
    SearchFlightPage(driver).search_flight("MAA", "LHR")

    logging.info("Waiting for search results and booking flight.")
    ResultPage(driver).wait_for_results_page()
    ResultPage(driver).click_book_button()

    logging.info("Reviewing traveler details.")
    booking_page = BookingPage(driver)
    booking_page.confirm_review_details()

    first_name = "Veera"
    last_name = "Sai"

    booking_page.fill_traveler_info(first_name, last_name)
    logging.info(f"Traveler info filled: {first_name} {last_name}")

    booking_page.book_and_pay()
    booking_page.handle_price_popup()

    logging.info("Confirming booking.")
    payment_page = PaymentPage(driver)
    payment_page.confirm_booking()

    logging.info("Verifying traveler name after booking.")
    if payment_page.verify_traveller_name(first_name, last_name):
        logging.info("Traveler name verification successful. Proceeding to payment.")
        payment_page.make_payment()
        payment_page.confirm_payment()
    else:
        logging.error("Traveler name verification failed.")
        raise AssertionError("Traveler name mismatch")
