from typing import Any, Dict, List, Union

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def currency() -> List[Dict[str, Union[int, str, Dict[str, Union[str, Dict[str, str]]]]]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


def test_filter_by_currency(currency: List[Dict[str, Any]]) -> None:
    result_currency: List[Dict[str, Any]] = list(
        filter(lambda x: x["operationAmount"]["currency"]["code"] == "USD", currency)
    )
    assert result_currency == currency


def test_invalid_filter() -> None:
    with pytest.raises(ValueError):
        list(filter_by_currency([]))


@pytest.fixture()
def descriptions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


def test_transaction_descriptions(descriptions: List[Dict[str, Any]]) -> None:
    expected_descriptions = ["Перевод с карты на карту"]  # Ожидаемые значения
    result_descriptions = transaction_descriptions(descriptions)
    assert list(result_descriptions) == expected_descriptions


def test_invalid_descriptions() -> None:
    with pytest.raises(ValueError):
        list(transaction_descriptions([]))


@pytest.mark.parametrize("card_number_generation", [["0000 0000 0000 0001"]])
def test_card_number_generator(card_number_generation: List[str]) -> None:
    assert list(card_number_generator(1, 1)) == card_number_generation
