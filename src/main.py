import random
from src.widget import mask_account_card, get_data
unique_list = ['Счет 73654108430135874305', 'Visa Platinum 7000792289606361', 'Maestro 7000792289606361']
print(mask_account_card(random.choice(unique_list)))
print(get_data('2024-03-11T02:26:18.671407'))

