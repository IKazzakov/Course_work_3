from datetime import datetime


class Operation:
    def __init__(self, operation: dict):
        self.id = operation['id']
        self.date = operation['date']
        self.state = operation['state']
        self.operation_amount = operation['operationAmount']
        self.description = operation['description']
        self.from_info = operation.get('from')
        self.to_info = operation['to']

    def __repr__(self):
        return (f'''Operation('
                'id = {self.id}, date = {self.date}, 
                state = {self.state}, operation_amount = {self.operation_amount}),
                description = {self.description}, from_ = {self.from_info}, to = {self.to_info}
''')

    def get_date(self):
        """Функция перевода исходного формата даты в формат ДД.ММ.ГГГГ"""
        date_base = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        date_correct_format = date_base.strftime('%d.%m.%Y')
        return date_correct_format

    def get_description(self):
        """Получаем описание операции"""
        return self.description

    def get_masked_from_info(self):
        """Получаем информацию по отправителю с зашифрованными данными карты или счета"""
        if self.from_info is None:
            return 'Нет данных'
        from_info_list = self.from_info.split()
        card_or_bill_name = ' '.join(from_info_list[:-1])
        card_or_bill_number = from_info_list[-1]
        if card_or_bill_name == 'Счет':
            return f'{card_or_bill_name} **{card_or_bill_number[-4:]}'
        else:
            return (f'{card_or_bill_name} {card_or_bill_number[:4]}'
                    f' {card_or_bill_number[4:6]}** **** {card_or_bill_number[-4:]}')

    def get_masked_to_info(self):
        """Получаем информацию по получателю с зашифрованными данными карты или счета"""
        to_info_list = self.to_info.split()
        card_or_bill_name = ' '.join(to_info_list[:-1])
        card_or_bill_number = to_info_list[-1]
        if card_or_bill_name == 'Счет':
            return f'{card_or_bill_name} **{card_or_bill_number[-4:]}'
        else:
            return (f'{card_or_bill_name} {card_or_bill_number[:4]} '
                    f'{card_or_bill_number[4:6]}** **** {card_or_bill_number[-4:]}')

    def get_operation_amount(self):
        """Получаем информацию по сумме операции и валюте"""
        amount = self.operation_amount['amount']
        currency = self.operation_amount['currency']['name']
        return f'{amount} {currency}'

    def get_operation_info(self):
        """Выводим информацию об операции в требуемом формате"""
        return f'''
        {self.get_date()} {self.get_description()}
        {self.get_masked_from_info()} -> {self.get_masked_to_info()}
        {self.get_operation_amount()}
'''
