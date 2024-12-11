def mask_account_card(input_string: str) -> str:
    """Функция которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if not input_string:
        raise ValueError("Входная строка не может быть пустой")
    digits = ""
    letters = ""
    for char in input_string:
        if char.isdigit():
            digits += char
        elif char.isalpha() or char == " ":
            letters += char
        else:
            raise ValueError("Недопустимый символ при вводе карты.")
    letters = " ".join(letters.split())
    if len(digits) != 16 and len(digits) != 20:
        raise ValueError("Неверная длина номера карты или счёта. Должно быть 16 цифр или 20 цифр.")

    if len(digits) == 16:
        return letters + " " + digits[:4] + " " + digits[4:6] + "** ****" + digits[-4:]
    elif len(digits) == 20:
        return letters + " **" + digits[-4:]
    else:
        return ""


def get_data(data: str) -> str:
    if len(data) == 26:
        date_str = data.split("T")[0]
        year, month, day = date_str.split("-")
        formatted_date = f"{day}.{month}.{year}"
        return formatted_date
    else:
        raise ValueError("Недопустимый формат даты и времени")


print(get_data("2024-03-11T02:26:18.671407"))
