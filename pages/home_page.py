from pages.city_page import CityPage


class HomePage:

    def __init__(self, page):
        self.page = page
        self.city_input = page.locator('//input[@data-test-id="city-selector-input"]')
        self.see_bikes_button = page.locator("//button[@data-test-id='city-selector-submit']")

    def select_city(self, city):
        self.city_input.fill(city)
        with self.page.expect_navigation():
            self.see_bikes_button.click()
        return CityPage(self.page)
