def get_mask_card_number(a: str) -> str:
    """Функция принимает на вход номер карты и возвращает её в виде маску
    в формате XXXX XX** **** XXXX"""

    masks_number = a[:4] + "-" + a[4:6] + "**-" + "****-" + a[-4:]
    return masks_number


def get_mask_account(a: str) -> str:
    """Функция принимает на вход номер счёта и возвращает её в виде маски
    в формате **ХХХХ"""
    masks_account = "**" + a[-4:]
    return masks_account
