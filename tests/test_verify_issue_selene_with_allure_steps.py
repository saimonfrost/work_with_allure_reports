"""
Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
Лямбда шаги через with allure.step
"""
import allure
from selene import browser, by, have


def test_verify_issue(window_config):

    with allure.step("Открываем репозиторий allure-example"):
        browser.open('https://github.com/')
        browser.element('.header-search-button').click()
        browser.element('.QueryBuilder-InputWrapper #query-builder-test').type(
            "eroshenkoam/allure-example").press_enter()
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем страницу Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие issue с заголовком 'Issue_created_to_test_allure_reports' "):
        browser.element('.js-navigation-container').should(have.text('Issue_created_to_test_allure_reports'))
