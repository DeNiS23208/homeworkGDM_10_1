def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает его в виде маски
    в формате XXXX XX** **** XXXX"""

    # Проверяем, что строка состоит только из цифр
    if not card_number.isdigit():
        raise ValueError('Неверный формат карты. Номер карты должен содержать только цифры.')

    # Проверяем длину номера карты
    if len(card_number) != 16:
        raise ValueError('Неверная длина номера карты. Должно быть 16 цифр.')

    # Формируем маскированный номер карты
    masked_number = card_number[:4] + "-" + card_number[4:6] + "**-" + "****-" + card_number[-4:]
    return masked_number


def get_mask_account(account_card: str) -> str:
    """Функция принимает на вход номер счёта и возвращает её в виде маски
    в формате **ХХХХ"""
    if not account_card.isdigit():
        raise ValueError('Неверный формат счёта. Номер счёта должен содержать только цифры.')

    if len(account_card) != 16:
        raise ValueError('Неверная длина номера счёта. Должно быть 20 цифр.')

    masks_account = "**" + account_card[-4:]
    return masks_account
