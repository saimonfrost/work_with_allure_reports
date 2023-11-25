"""
Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
Лямбда шаги через with allure.step
"""
from work_with_allure_reports.model.pages.AllureRepositoryPage import AllureRepository
import allure


def test_verify_issue(window_config):
    allure_repository = AllureRepository()

    with allure.step("Открываем репозиторий allure-example"):
        allure_repository.open()

    with allure.step("Открываем страницу Issues"):
        allure_repository.issues()

    with allure.step("Проверяем наличие issue с заголовком 'Issue_created_to_test_allure_reports' "):
        allure_repository.should_have_issue('Issue_created_to_test_allure_reports')
