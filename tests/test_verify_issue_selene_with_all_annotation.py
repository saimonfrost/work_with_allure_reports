"""
Написать тест на проверку названия Issue в репозитории через Web-интерфейс.
Шаги с декоратором @allure.step со всеми аннотациями
"""
import allure
from allure_commons.types import Severity

from work_with_allure_reports.model.pages.AllureRepositoryPage import AllureRepository


@allure.tag("web")
@allure.id(100)
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Федоров Семен')
@allure.feature("Задачи в репозитории")
@allure.title("Наличие Issue в репозитории после ее создания")
@allure.story("После создании задачи, задача должна находится в списке задач Issue")
@allure.description("Открываем репозиторий и находим внутри созданную задачу")
@allure.issue("/work_with_allure_reports")
@allure.epic("Регресс")
@allure.parent_suite("Создание задачи в репозитории")
def test_verify_issue(window_config):
    allure_repository = AllureRepository()

    allure_repository.open()
    allure_repository.issues()

    allure_repository.should_have_issue('Issue_created_to_test_allure_reports')
