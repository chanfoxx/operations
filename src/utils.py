import json
from datetime import datetime


class JsonFileMixin:
    """ Класс-миксин работы с json-файлами. """
    def __init__(self, filename) -> None:
        """
        Создание экземпляра класса JsonFileMixin.

        :param filename: json-файл.
        """
        self.filename = filename

    def operations_file(self):
        """ Возвращает файл json с данными по банковским операциям. """
        try:
            with open(self.filename, encoding='utf-8') as file:
                operations = json.load(file)
        except FileNotFoundError:
            return f"File {self.filename} not found."
        except json.JSONDecodeError:
            return f"Error decode JSON file {self.filename}."
        else:
            return operations


class Operation(JsonFileMixin):
    """ Класс для банковских операций. """
    def __init__(self, filename):
        """ Создание экземпляра класса Operation. """
        super().__init__(filename)

    def get_executed_operations(self):
        """ Выбирает и возвращает выполненные операции. """
        operations = self.operations_file()
        executed_operations = [operation for operation in operations
                               if operation.get('state') == 'EXECUTED']

        return executed_operations

    @staticmethod
    def get_sorted_operations(operations):
        """
        Сортирует операции по дате и
        возвращает список пяти последних операций.
        """
        sorted_operations = sorted(
            operations, key=lambda operation: operation['date'],
            reverse=True
        )[:5]

        return sorted_operations

    @staticmethod
    def get_format_date(date_str):
        """ Возвращает отформатированную дату вида ДД.ММ.ГГГГ. """
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        return date_obj.strftime("%d.%m.%Y")

    @staticmethod
    def mask_card_number(card_number):
        """
        Возвращает замаскированные номера счетов
        и карт отправителя/получателя (если они существуют).
        """
        if 'Счет' in card_number:
            masked_number = card_number[:5] + '**' + card_number[-4:]
            return masked_number
        elif 'Unknown' in card_number:
            return 'Unknown'
        else:
            masked_number = card_number[:-16] + card_number[-16:-12] + ' ' + \
                            card_number[-12:-10] + '** **** ' + card_number[-4:]
            return masked_number
