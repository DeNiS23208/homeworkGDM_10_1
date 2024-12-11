from typing import Any, Dict, List


def filter_by_state(find_state: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению."""
    kol = 0
    for find in find_state:
        if find["state"] != "EXECUTED" and find["state"] != "CANCELED":
            raise ValueError('Данные отсутствуют')

    result_filter_state = []

    for find in find_state:
        if find["state"] == state:
            result_filter_state.append(find)

    return result_filter_state


def sort_by_date(sort_data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция должна возвращать новый список, отсортированный по дате (date)."""

    sorted_date = sorted(sort_data, key=lambda x: x["date"], reverse=reverse)

    return sorted_date


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(sort_by_date(transactions))
print(filter_by_state(transactions))
