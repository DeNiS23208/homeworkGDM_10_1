import pytest
from src.processing import filter_by_state, sort_by_date
from typing import Any, Dict, List


@pytest.fixture
def transactions():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def invalid_transactions():
    return [
        {"id": 41428829, "state": "EXECUT", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXEUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CAELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANLED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
    ("NON_EXISTENT", 0)
])
def test_filter_by_state(transactions, state, expected_count):
    result = filter_by_state(transactions, state)
    assert len(result) == expected_count


def test_invalid_state_raises_value_error(invalid_transactions):
    with pytest.raises(ValueError):
        filter_by_state(invalid_transactions)


@pytest.fixture
def transactions_valid() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Фикстура для некорректных транзакций
@pytest.fixture
def transactions_invalid() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "da3e": "not_a_date"},  # Неверное значение даты
        {"id": 2, "state": "CANCELED", "da1e": "2018-10-14"},  # Верное значение, но некорректный тип в контексте
        {"id": 3, "state": "EXECUTED", "da5e": "07-03-2019 18:35:29"},  # Неверный формат даты
    ]


# Тест для проверенных транзакций
def test_sort_by_date_valid(transactions_valid):
    sorted_transactions = sort_by_date(transactions_valid, reverse=False)
    assert sorted_transactions[0]["id"] == 939719570  # Самая ранняя дата
    assert sorted_transactions[-1]["id"] == 41428829  # Самая поздняя дата


# Тест для некорректных транзакций
def test_sort_by_date_invalid(transactions_invalid):
    with pytest.raises(ValueError):  # мы ожидаем ValueError из-за некорректных дат
        sort_by_date(transactions_invalid)
