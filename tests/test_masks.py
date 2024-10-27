import pytest
from main.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    'test_input, expected',
    (
            ("7000792289606361", "7000 79** **** 6361"),
            ("9213882192018312", "9213 88** **** 8312"),
    )
)
def test_get_mask_card_number(test_input, expected):
    assert get_mask_card_number(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
            ("123456789", "6789"),
            ("9876543210", "3210"),
            ("   1234   ", "1234"),  # Пробелы вокруг
            ("1234 5678 9012", "9012"),  # Пробелы внутри

    )
)
def test_get_mask_account(test_input, expected):
    assert get_mask_account(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected_message',
    (
            ("123", 'Номер счета должен содержать не менее 4 цифр.'),
            ("", 'Номер счета должен содержать не менее 4 цифр.'),
            ("   ", 'Номер счета должен содержать не менее 4 цифр.'),
            ("12", 'Номер счета должен содержать не менее 4 цифр.'),
    )
)
def test_get_mask_account_exceptions(test_input, expected_message):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(test_input)
    assert str(exc_info.value) == expected_message
