from Utils import last_five_operations

def test_get_executed_operation():
    """Проверяем статус операций в списке выполненных операций"""
    executed_operations = last_five_operations.get_executed_operations()
    assert executed_operations[0]['state'] == 'EXECUTED'
    assert executed_operations[1]['state'] == 'EXECUTED'


def test_get_last_five_operation():
    """Проверяем длинну списка выполненных операций"""
    assert len(last_five_operations.get_last_five_operation()) == 5
