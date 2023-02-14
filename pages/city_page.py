from pages.subscription_page import SubscriptionPage


class CityPage:
    TITLE = 'Our bikes in London'

    def __init__(self, page):
        self.page = page
        self.page.wait_for_load_state("networkidle")
        self.filters = page.locator("//input[@name='product-filter']")
        self.bikes = page.locator("//li[@data-test-id='city-product-list-item']")
        self.subscribe_power_one_button = page.locator(
            "//a[@data-test-id='product-cta-link' and contains(@href, 'power-1')]")
        self.apps_stores_link_section = page.locator("//div[contains(@class,'AppStoreLinks')]")

    def subscribe_for_bike(self):
        with self.page.expect_navigation():
            self.subscribe_power_one_button.click()
        return SubscriptionPage(self.page)
