# def get_mask_card_number(num_card: str) -> str:
#     """Функция принимает на вход тип карты, номер карты и
#     возвращает её в виде маски в формате XXXX XX** **** XXXX"""
#     list_card = []
#     for i in num_card:
#         list_card.append(i)
#     one_space = list_card.index(' ')
#     name_type_card = list_card[:one_space]
#     if ''.join(name_type_card) == 'Счет':
#         print(''.join(name_type_card) + ' **' + num_card[-4:])
#     elif ''.join(name_type_card) == 'Maestro':
#         print(''.join(name_type_card) +
#                                    num_card[one_space:one_space + 5] + ' ' + num_card[
#                               one_space + 5:one_space + 7] + '** ****' + num_card[#                                                                                                                              -4:])
#     elif ''.join(name_type_card) == 'Visa':
#         print(''.join(name_type_card) + num_card[one_space:one_space + 9] + num_card[
#                                                                             one_space + 9:one_space + 14] + ' ' + num_card[
#                                                                                                                   one_space + 14:one_space + 16] + '** ****' + num_card[
#                                                                                                                                                                -4:])

# def get_mask_card_number(a: str) -> str:
#     """Функция принимает на вход номер карты и возвращает её в виде маску
#     в формате XXXX XX** **** XXXX"""
#
#     masks_number = a[:4] + "-" + a[4:6] + "**-" + "****-" + a[-4:]
#     return masks_number
#
#
# def get_mask_account(a: str) -> str:
#     """Функция принимает на вход номер счёта и возвращает её в виде маски
#     в формате **ХХХХ"""
#     masks_account = "**" + a[-4:]
#     return masks_account
