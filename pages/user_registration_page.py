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

    def fill_registration_form(self, user):
        self.day.select_option(user["day"])
        self.month.select_option(user["month"])
        self.year.select_option(user["year"])
        self.firstname.fill(user["firstname"])
        self.lastname.fill(user["lastname"])
        self.female_gender.check()
        self.post_code.fill(user["post_code"])
        self.height.fill(user["height"])
        self.street.fill(user["street"])
        self.house.fill(user["house"])
        self.city.fill(user["city"])
        self.email.fill(user["email"])
        self.phone.fill(user["phone"])
        self.terms_checkbox.check()

    def go_back(self):
        with self.page.expect_navigation():
            self.back_button.click()
        from pages.home_page import HomePage
        return HomePage(self.page)
