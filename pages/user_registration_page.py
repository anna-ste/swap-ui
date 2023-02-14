class UserRegistrationPage():
    def __init__(self, page):
        self.page = page
        self.page.wait_for_load_state("networkidle")
        self.firstname = page.locator("//input[@name='firstname']")
        self.lastname = page.locator("//input[@name='lastname']")
        self.phone = page.locator("//input[@name='telephoneNumber1']")
        self.email = page.locator("//input[@name='email']")
        self.day = page.locator("//select[@name='Day']")
        self.month = page.locator("//select[@name='Month']")
        self.year = page.locator("//select[@name='Year']")
        self.city = page.locator("//input[@name='city']")
        self.house = page.locator("//input[@name='houseNumber']")
        self.street = page.locator("//input[@name='street']")
        self.height = page.locator("//input[@name='height']")
        self.male_gender = page.locator("//input[@id='gender-male']")
        self.female_gender = page.locator("//label[@for='gender-female']")
        self.other_gender = page.locator("//input[@id='gender-other']")
        self.house_addition = page.locator("//input[@name='houseNumberSuffix']")
        self.post_code = page.locator("//input[@name='postalCode']")
        self.terms_checkbox = page.locator("//label[@for='terms-checkbox']")
        self.back_button = page.locator("div.back-button")
        self.next_button = page.locator("//button[contains(@data-met, 'Personal details')]")

    def fill_registration_form(self):
        self.day.select_option("1")
        self.month.select_option("February")
        self.year.select_option("2000")
        self.firstname.fill('Anna')
        self.lastname.fill('Filippova')
        self.female_gender.check()
        self.post_code.fill('W1U 8ED')
        self.height.fill('174')
        self.street.fill('Herengracht')
        self.house.fill('71')
        self.city.fill('London')
        self.email.fill('bla@test.me')
        self.phone.fill('123')
        self.terms_checkbox.check()

    def go_back(self):
        with self.page.expect_navigation():
            self.back_button.click()
        from pages.home_page import HomePage
        return HomePage(self.page)
