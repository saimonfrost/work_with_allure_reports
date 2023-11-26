import allure
from selene import browser, by, have
from allure import attachment_type


class AllureRepository:
    def __init__(self):
        pass

    @allure.step("Открываем репозиторий allure-example")
    def open(self):
        browser.open('https://github.com/')
        browser.element('.header-search-button').click()
        browser.element('.QueryBuilder-InputWrapper #query-builder-test').type(
            "eroshenkoam/allure-example").press_enter()
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
        allure.attach("github.com/eroshenkoam/allure-example", name="Сайт", attachment_type=attachment_type.TEXT)
        return self

    @allure.step("Открываем страницу Issues")
    def issues(self):
        browser.element("#issues-tab").click()
        return self

    @allure.step("Проверяем наличие issue с заголовком 'Issue_created_to_test_allure_reports' ")
    def should_have_issue(self, value):
        browser.element('.js-navigation-container').should(have.text(value))
        return self
