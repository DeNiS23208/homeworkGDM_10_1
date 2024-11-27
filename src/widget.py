from src.masks import get_mask_card_number, get_mask_account
"""Функция которая умеет обрабатывать информацию как о картах, так и о счетах"""
def mask_account_card(card_info: str) -> str:
    one_space = card_info.index(' ')
    if card_info[:one_space] == 'Maestro':
        return card_info[:one_space] + get_mask_card_number(card_info[one_space:])
    elif card_info[:one_space] == 'Visa':
        return card_info[:one_space + 9] + get_mask_card_number(card_info[one_space + 9:])
    elif card_info[:one_space] == 'Счет':
        return card_info[:one_space] + ' ' + get_mask_account(card_info[one_space:])
    else:
        return 'Нет такого типа карты'

def get_data(data: str) -> str:
    date_str = data.split("T")[0]
    return date_str