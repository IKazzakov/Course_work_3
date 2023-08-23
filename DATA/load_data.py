import json
import requests
import os


def load_data(path, url = None):
    """
    Функция загрузки данных из файла
    :return: список с набором данных
    """

    if os.path.exists(path):
        with open(path, encoding='utf-8') as file:
            return json.load(file)
    elif url != None:
        response = requests.get(url)
        return response.json()
    else:
         return 'Не удалось найти файл'
