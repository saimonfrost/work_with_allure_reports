"""
Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
Шаги с декоратором @allure.step
"""
from work_with_allure_reports.model.pages.AllureRepositoryPage import AllureRepository


def test_verify_issue(window_config):
    allure_repository = AllureRepository()

    allure_repository.open()
    allure_repository.issues()

    allure_repository.should_have_issue('Issue_created_to_test_allure_reports')
