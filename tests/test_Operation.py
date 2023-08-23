from Operation import Operation
import pytest


@pytest.fixture
def class_instance():
    """Создаем экземпляр класса перед каждым тестом"""
    example_operation = {
        "id": 957763565,
        "state": "EXECUTED",
        "date": "2019-01-05T00:52:30.108534",
        "operationAmount": {
            "amount": "87941.37",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 46363668439560358409",
        "to": "Счет 18889008294666828266"
    }
    return Operation(example_operation)


def test_get_date(class_instance):
    """Проверка получения даты в заданном формате"""
    assert class_instance.get_date() == '05.01.2019'

def test_get_description(class_instance):
    """Проверка получения описания операции"""
    assert class_instance.get_description() == 'Перевод со счета на счет'


def test_get_masked_from_info(class_instance):
    """Проверка получения информации отправителя в заданном формате"""
    assert class_instance.get_masked_from_info() == "Счет **8409"


def test_get_masked_to_info(class_instance):
    """Проверка получения информации получателя в заданном формате"""
    assert class_instance.get_masked_to_info() == "Счет **8266"


def test_get_operation_amount(class_instance):
    """Проверка получения информации о сумме и валюте операции"""
    assert class_instance.get_operation_amount() == "87941.37 руб."


def test_get_operation_info(class_instance):
    """Проверка корректного вывода  информации по операции"""
    operation_info = f"""
        05.01.2019 Перевод со счета на счет
        Счет **8409 -> Счет **8266
        87941.37 руб.
"""
    assert class_instance.get_operation_info() == operation_info
