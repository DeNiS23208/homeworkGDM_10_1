from typing import List, Dict


def filter_by_state(find_state: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению."""

    result_filter_state = []

    for find in find_state:
        if find['state'] == state:
            result_filter_state.append(find)

    return result_filter_state
