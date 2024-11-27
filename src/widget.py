def get_mask_card_number(num_card: str) -> str:
    """Функция принимает на вход тип карты, номер карты и возвращает её в виде маски
    в формате XXXX XX** **** XXXX"""
    list_card = []
    for i in num_card:
        list_card.append(i)
    one_space = list_card.index(' ')
    name_type_card = list_card[:one_space]
    if ''.join(name_type_card) == 'Счет':
        print(''.join(name_type_card) + ' **' + num_card[-4:])
    elif ''.join(name_type_card) == 'Maestro':
        print(''.join(name_type_card) + num_card[one_space:one_space + 5] + ' ' + num_card[
                                                                                  one_space + 5:one_space + 7] + '** ****' + num_card[
                                                                                                                             -4:])
    elif ''.join(name_type_card) == 'Visa':
        print(''.join(name_type_card) + num_card[one_space:one_space + 9] + num_card[
                                                                            one_space + 9:one_space + 14] + ' ' + num_card[
                                                                                                                  one_space + 14:one_space + 16] + '** ****' + num_card[
                                                                                                                                                               -4:])

def get_data(info_clock: str) -> str:
    """Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
     и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    print(info_clock[9:11] + '.' + info_clock[6:8] + '.' + info_clock[1:5])