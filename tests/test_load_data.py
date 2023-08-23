import DATA.data_address
from DATA import load_data


def test_load_data():
    """Проверка функции загрузки данных"""
    assert load_data.load_data(' ') == 'Не удалось найти файл'
    assert len(load_data.load_data(' ', DATA.data_address.data_url)) > 0
