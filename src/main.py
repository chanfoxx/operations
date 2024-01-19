from src.utils import Operation


filename = 'operations.json'
# Создаем экземпляр класса Operation, открываем json-файл.
operations = Operation(filename)
# Выбираем выполненные операции.
ex_operations = operations.get_executed_operations()
# Сортирует операции по дате и возвращает список пяти последних операций.
sorted_operations = operations.get_sorted_operations(ex_operations)

# Проходимся циклом по списку отсортированных операций и форматируем данные.
for operation in sorted_operations:
    # Форматируем дату в вид ДД.ММ.ГГГГ.
    date = operations.get_format_date(operation['date'][:10])
    # Выбираем описание банковской операции.
    description = operation['description']
    # Номер "от" кого перевод (если он виден) и
    # номер "кому" перевод
    from_card = operation.get('from', 'Unknown')
    to_card = operation['to']
    # Сумма и валюта перевода.
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    # Маскируем номера счетов/карт.
    masked_from = operations.mask_card_number(from_card)
    masked_to = operations.mask_card_number(to_card)

    print(f'{date} {description}\n{masked_from} -> {masked_to}\n{amount} {currency}\n')
