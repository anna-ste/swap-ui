from playwright.sync_api import expect

from pages.home_page import HomePage

PRICE = '£64.90'
CITY = 'London'


def test_select_city_order_bike_go_back(page, user):
    # go to start page
    page.goto('https://swapfiets.com/en-GB')
    home_page = HomePage(page)

    # select London in city selector field
    city_page = home_page.select_city(CITY)

    # check page and content according to selected city
    expect(city_page.page).to_have_title(city_page.TITLE)
    expect(city_page.filters).to_have_count(3)
    expect(city_page.bikes).to_have_count(4)
    expect(city_page.subscribe_power_one_button).to_be_visible()
    expect(city_page.apps_stores_link_section).to_be_visible()

    # subscribe to Power 1 bike
    subscription_page = city_page.subscribe_for_bike()

    # check subscription page
    expect(subscription_page.monthly_price_bar).to_contain_text(PRICE)
    expect(subscription_page.order_bike_button).to_be_visible()
    expect(subscription_page.membership_selector_group).to_be_visible()
    expect(subscription_page.bike_usage_selector_group).to_be_visible()
    expect(subscription_page.loyal_membership_option).to_be_checked()

    # order bike
    registration_page = subscription_page.order_bike()

    # fill personal details
    registration_page.fill_registration_form(user)

    # check form is filled and next registration step is available
    expect(registration_page.next_button).to_be_enabled()
    expect(registration_page.terms_checkbox).to_be_checked()

    # go back
    home_page = registration_page.go_back()

    # check page content
    expect(home_page.see_bikes_button).to_be_visible()
    expect(home_page.page).to_have_title(home_page.TITLE)
