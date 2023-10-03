from settings import PATH_WITH_FIXTURE
from src import utils


def test_operations_file():
    """
    Проверяет принадлежность файла к списку;
    Проверяет несуществующий файл.
    """
    assert isinstance(utils.operations_file(PATH_WITH_FIXTURE), list)
    assert utils.operations_file('file') is None


def test_last_operations(bank_fixture):
    """Проверяет возврат списка из 5-ти последних операций."""
    assert len(utils.last_operations(bank_fixture)) == 5


def test_mask_card_number(bank_fixture_2, bank_fixture_3, bank_fixture_4):
    """
    Проверяет маскировку номеров счетов
    и карт отправителя если они есть.
    """
    assert utils.mask_card_number(bank_fixture_2) == "Maestro 1596 83** **** 5199"
    assert utils.mask_card_number(bank_fixture_3) == "Счет **3493"
    assert utils.mask_card_number(bank_fixture_4) == "Unknown"


def test_mask_account_number(bank_fixture_3):
    """Проверяет маскировку номеров счетов."""
    assert utils.mask_account_number(bank_fixture_3) == "Счет **3493"


def test_format_date(bank_fixture_5):
    """Проверяет форматирование даты вида ДД.ММ.ГГГГ."""
    assert utils.format_date(bank_fixture_5) == '26.08.2019'


def test_format_operation(bank_fixture_6):
    """
    Проверяет форматирование данных для
    вывода информации пользователю.
    """
    formatted_operation = utils.format_operation(bank_fixture_6)
    assert formatted_operation == '26.08.2019 Перевод организации\n' \
                                  'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
                                  '31957.58 руб.\n'


def test_print_last_operations(bank_fixture_7):
    """
    Проверяет вывод данных пользователю
    в определенном формате.
    """
    assert utils.print_last_operations(bank_fixture_7) == ['08.12.2019 Открытие вклада\n'
                                                           'Unknown -> Счет **5907\n'
                                                           '41096.24 USD\n']
