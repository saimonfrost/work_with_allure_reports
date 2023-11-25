"""
Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
Чистый Selene
"""
from selene import browser, by, have


def test_verify_issue(window_config):
    browser.open('https://github.com/')
    browser.element('.header-search-button').click()
    browser.element('.QueryBuilder-InputWrapper #query-builder-test').type(
        "eroshenkoam/allure-example").press_enter()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()

    browser.element('.js-navigation-container').should(have.text('Issue_created_to_test_allure_reports'))
