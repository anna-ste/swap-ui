from pages.user_registration_page import UserRegistrationPage


class SubscriptionPage:

    def __init__(self, page):
        self.page = page
        self.page.wait_for_load_state("networkidle")
        self.monthly_price_bar = page.locator("//span[@data-test-id='priceBlueBar.monthly']")
        self.order_bike_button = page.locator("//button[@data-test-id='configure-submit-button']")
        self.membership_selector_group = page.locator("//div[@aria-label='Choose your membership']")
        self.bike_usage_selector_group = page.locator("//div[@data-test-id='heavy-use-radio-group']")
        self.no_heavy_usage_option = page.locator("//span[text()='No']/ancestor::label[@data-test-id='radio-button']")

    def order_bike(self):
        self.no_heavy_usage_option.click()
        with self.page.expect_navigation():
            self.order_bike_button.click()
        return UserRegistrationPage(self.page)
