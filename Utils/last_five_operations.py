from DATA import load_data, data_address
from operator import itemgetter


def get_executed_operations():
    """Получаем список выполненнных операций"""
    data = load_data.load_data(data_address.data_file, data_address.data_url)
    executed_operations = []
    for operation in data:
        if operation.get('state') == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def get_last_five_operation():
    """Получаем список последних пяти выполненных операций"""
    operations = get_executed_operations()
    sorted_operations = sorted(operations, key=itemgetter('date'), reverse=True)
    return sorted_operations[:5]