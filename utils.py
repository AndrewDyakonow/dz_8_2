import requests
from classes import Question


def get_json() -> list[dict]:
    """Прочитать данные с сайта"""
    response = requests.get('https://www.jsonkeeper.com/b/T812')
    return response.json()


def get_ex_class() -> list[Question]:
    """Создать список экземпляров класса"""
    data = get_json()
    list_ex = []
    for question in data:
        list_ex.append(Question(question.get('q'), question.get('d'), question.get('a')))

    return list_ex


def get_statistics(point: int, true_answers: int) -> None:
    """Показать статистику"""
    print(f'Вот и всё!')
    print(f'Отвечено {true_answers} вопроса из 5')
    print(f'Набрано баллов: {point}')
