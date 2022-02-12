"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count,min,max = 1,1,101 # задаём счётчик попыток и начальный диапазон для выбора чисел для угадывания
    
    while True:
        supposed_number = (min+max)/2  # предполагаемое число; здесь его не округляем, иначе при искомом числе равном 1 возникнет вечный цикл
        if round(supposed_number)==number:
            break
        count += 1
        if supposed_number>number:
            max=supposed_number
        else:
            min=supposed_number
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(count_ls)
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


#RUN
if __name__ == "__main__":
    score_game(random_predict)
