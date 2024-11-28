from typing import Tuple


def separate_digits_and_letters(input_string: str) -> Tuple[str, str]:
    """Функция которая умеет обрабатывать информацию как о картах, так и о счетах"""
    digits = ""
    letters = ""
    for char in input_string:
        if char.isdigit():
            digits += char
        elif char.isalpha():
            letters += char

    if len(digits) == 16:
        return letters, digits[:6] + "** ****" + digits[-4:]
    elif len(digits) == 20:
        return letters, "**" + digits[-4:]
    else:
        return letters, digits


def get_data(data: str) -> str:
    date_str = data.split("T")[0]
    year, month, day = date_str.split("-")
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date
