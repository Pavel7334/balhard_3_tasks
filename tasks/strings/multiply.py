"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Пользователь вводит строку и число n. Необходимо вернуть строку, которая
будет продублирована n раз

ПРИМЕРЫ
--------------------------------------------------------------------------------
- ('привет', 3) -> 'приветприветпривет'
- ('Маша', 2) -> 'МашаМаша'
"""


def multiply_str(user_string: str, n: str) -> str:
    """Дублирует строку n-раз

    :param user_string: строка для повторения
    :param n: число, сколько раз нужно продублировать

    :return: результирующая строка
    """

    return f'{user_string * int(n)}'


if __name__ == '__main__':
    string = input('Введите строку: ')
    numb = input('Сколько раз продублировать: ')
    print(f'Склеенная строка: {multiply_str(string, numb)}')
