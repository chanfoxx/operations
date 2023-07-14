import json
from datetime import datetime


filename = 'operations.json'
def operations_file(filename):
    """
    Возвращает файл json с
    данными по банковским операциям.
    """
    with open(filename, encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def get_date(operations):
    """Возращает значение с датой по ключу."""
    return operations['date']


def last_operations(operations):
    """
    Выбирает выполненные операции, сортирует
    их по дате и возвращает список 5-ти последних операций.
    """
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=get_date, reverse=True)
    five_last_operations = sorted_operations[:5]
    return five_last_operations


def mask_card_number(card_number):
    """Возвращает замаскированные номера счетов и карт отправителя."""
    if 'Счет' in card_number:
        card_number = card_number.replace(' ', '')
        masked_number = card_number[:4] + ' ' + '**' + card_number[-4:]
        return masked_number
    elif 'Unknown' in card_number:
        return 'Unknown'
    else:
        masked_number = card_number[:-16] + card_number[-16:-12] + ' ' + \
                        card_number[-12:-10] + '** **** ' + card_number[-4:]
        return masked_number


def mask_account_number(account_number):
    """Возвращает замаскированные номера счетов получателя."""
    masked_number = account_number[:5] + '**' + account_number[-4:]
    return masked_number


def print_last_operations(file_last_operations):
    """
    Выводит пользователю 5 последних
    операций в определенном формате.
    """
    for operation in file_last_operations:
        date_str = operation['date'][:10]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        date = date_obj.strftime("%d.%m.%Y")

        description = operation['description']

        from_card = operation.get('from', 'Unknown')
        to_card = operation['to']

        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        masked_from = mask_card_number(from_card)
        masked_to = mask_account_number(to_card)

        print(f'''{date} {description}
{masked_from} -> {masked_to}
{amount} {currency}\n''')


operations = operations_file(filename)
last_five_operations = last_operations(operations)
print_last_operations(last_five_operations)

# Реализуйте функцию, которая выводит на экран список
# из 5 последних выполненных клиентом операций в формате:
#
# <дата перевода> <описание перевода>
# <откуда> -> <куда>
# <сумма перевода> <валюта>

# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.
