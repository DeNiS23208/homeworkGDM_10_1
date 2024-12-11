from src.masks import get_mask_account, get_mask_card_number
import pytest


@pytest.fixture
def num_card():
    return ['1234567812345678', '8765432187654321']


@pytest.fixture
def num_invalid_number_card():
    return ['12345678', '12345678123456789', '1234-abcd-5678']


@pytest.fixture
def num_account():
    return ['1234567812345678', '8765432187654321']


@pytest.fixture
def num_invalid_account_card():
    return ['12345678', '1234567812345678943242342', '1234-abcd-5678-scsd']


@pytest.mark.parametrize("card_number, expected", [
    ('1234567812345678', '1234-56**-****-5678'),
    ('8765432187654321', '8765-43**-****-4321')])
def test_mask_card_number(num_card, card_number, expected):
    result = get_mask_card_number(card_number)
    assert result == expected


def test_mask_card_invalid_len_number(num_invalid_number_card):
    for card_number in num_invalid_number_card:
        with pytest.raises(ValueError):
            get_mask_card_number(card_number)


@pytest.mark.parametrize("account_card, expected", [
    ('1234567812345678', '**5678'),
    ('8765432187654321', '**4321')])
def test_get_mask_account(num_account, account_card, expected):
    result = get_mask_account(account_card)
    assert result == expected


def test_get_mask_invalid_len_account(num_invalid_account_card):
    for num_acc in num_invalid_account_card:
        with pytest.raises(ValueError):
            get_mask_account(num_acc)
