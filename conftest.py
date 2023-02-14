import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=False)
        context = browser.new_context()

        # add consent cookies
        context.add_cookies([{'name': 'CookieConsent',
                              'value': '{stamp:%27gbo7eV4cypV28EbMhnSTvVoyZ6PUIsnQwehj5C3XLqRxn0JeUv27Dw==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1676332448497000%2Cregion:%27nl%27}',
                              'url': 'https://swapfiets.co.uk', 'expirationDate': '2528417744'}])
        context.add_cookies([{'name': 'CookieConsent',
                              'value': '{stamp:%27gbo7eV4cypV28EbMhnSTvVoyZ6PUIsnQwehj5C3XLqRxn0JeUv27Dw==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1676332448497000%2Cregion:%27nl%27}',
                              'url': 'https://account.swapfiets.com', 'expirationDate': '2528417744'}])

        # create a new page inside context.
        page = context.new_page()
        yield page
        context.close()
