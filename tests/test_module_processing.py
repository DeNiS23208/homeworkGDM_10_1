import pytest
from src.processing import filter_by_state


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
