from Operation import Operation
from Utils import last_five_operations


def main():
    """Основная функция, выводит на экран последние 5 выполненных операций
    в требуемом формате"""
    # Получаем список последних 5 выполненных операций
    operations = last_five_operations.get_last_five_operation()
    # Создаем список экземпляров класса
    operation_class_ex = [Operation(i) for i in operations]
    # Выводим последние 5 выполненных операций на экран
    for operation in operation_class_ex:
        print(operation.get_operation_info(), end='')


if __name__ == '__main__':
    main()
