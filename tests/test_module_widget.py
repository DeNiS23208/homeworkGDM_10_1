from typing import List

import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** ****6361"),
        ("MasterCard 5555444433338888", "MasterCard 5555 44** ****8888"),
        ("American Express 3782823244440005", "American Express 3782 82** ****0005"),
        ("Visa Classic 6011113232231117", "Visa Classic 6011 11** ****1117"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
    ],
)
def test_mask_account_card_various_types(input_string: str, expected: str) -> None:
    result = mask_account_card(input_string)
    assert result == expected


@pytest.fixture
def num_invalid_number_card() -> List[str]:
    return ["12345678", "1234567812345678932", "1234-abcd-5678"]


def test_invalid_card_and_account(num_invalid_number_card: List[str]) -> None:
    for card_number in num_invalid_number_card:
        with pytest.raises(ValueError):
            mask_account_card(card_number)


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2012-05-10T02:22:11.631407", "10.05.2012"),
        ("1999-12-31T23:59:59.124253", "31.12.1999"),
        ("2021-07-04T18:25:43.213144", "04.07.2021"),
        ("2000-02-29T12:01:01.321321", "29.02.2000"),
    ],
)
def test_get_data(input_date: str, expected_output: str) -> None:
    result = get_data(input_date)
    assert result == expected_output


# Тестирование обработки некорректного формата
@pytest.mark.parametrize(
    "input_date",
    [
        "15.10.2023",  # неверный формат
        "2023/10/15T12:34:56",  # неверный разделитель
        "2023-10-15",  # отсутствует время
        "2023-10-32T12:34:56",  # некорректная дата (нет 32-го дня)
    ],
)
def test_get_data_invalid_format(input_date: str) -> None:
    with pytest.raises(ValueError):  # Предполагаем, что вы должны выбросить ValueError для некорректного формата
        get_data(input_date)
