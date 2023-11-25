from selene import browser, by, have


class AllureRepository:
    def __init__(self):
        pass

    def open(self):
        browser.open('https://github.com/')
        browser.element('.header-search-button').click()
        browser.element('.QueryBuilder-InputWrapper #query-builder-test').type(
            "eroshenkoam/allure-example").press_enter()
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
        return self

    def issues(self):
        browser.element("#issues-tab").click()
        return self

    def should_have_issue(self, value):
        browser.element('.js-navigation-container').should(have.text(value))
        return self
