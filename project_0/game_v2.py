"""Игра угадай число
Компьютер сам загадывает и сам угадывает число

"""

import numpy as np


def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
        
    """
    
    # Задаём счётчик попыток и начальный диапазон выбора чисел для угадывания.
    count, min, max = 1, 1, 101
    
    while True:
        # Задаём предполагаемое число.
        # Здесь его не округляем, иначе при искомом числе равном 1 возникнет вечный цикл.
        supposed_number = (min+max) / 2
        if round(supposed_number) == number:
            break
        count += 1
        if supposed_number > number:
            # Устанавливаем новую верхнюю границу диапазона выбора числа.
            max = supposed_number
        else:
            # Устанавливаем новую нижнюю границу диапазона выбора числа.
            min = supposed_number
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм.

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
        
    """
    
    count_ls = []
    # Фиксируем сид для воспроизводимости.
    #np.random.seed(1)
    # Загадываем список чисел.
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


#RUN
if __name__ == "__main__":
    score_game(random_predict)
