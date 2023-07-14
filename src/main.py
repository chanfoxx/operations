from src import utils


# вводим переменную для файла с данными и
# загружаем его с помощью функции.
filename = 'operations.json'
operations = utils.operations_file(filename)

# получаем список 5-ти последних банковских операций.
last_five_operations = utils.last_operations(operations)

# выводим пользователю 5 выполненных последних операций.
utils.print_last_operations(last_five_operations)
