# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)

[2. Какой кейс решаем](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D0%BA%D0%B0%D0%BA%D0%BE%D0%B9-%D0%BA%D0%B5%D0%B9%D1%81-%D1%80%D0%B5%D1%88%D0%B0%D0%B5%D0%BC)

[3. Краткая информация о данных](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%25%D0%9A%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

[4. Этапы работы над проектом](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)

[5. Результат](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82)

[6. Выводы](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B)

## Описание проекта
Угадать случайное число за минимальное количество попыток.

:arrow_up:[к оглавлению](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

## Какой кейс решаем
Написать программу, которая находит случаное заданное число за минимальное количество попыток.

**Условия соревнования:**
- Компьютер задаёт случайное чило в диапазоне от 1 до 100
- Компютер может сообщать результат сравнения проверяемого числа с заданным: оно больше, меньше или равно заданному.

**Метрика качества**

Результат считается приемлемым, если при поиске 1000 чисел программа находит число в среднем не более, чем за 20 попыток.

**Цель**

Улучшить навык написания хорошего код на Python.

:arrow_up:[к оглавлению](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

## Краткая информация о данных
Программа не использует внешние данные.

:arrow_up:[к оглавлению](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

## Этапы работы над проектом
1. Написание первоначальной редакции кода.
2. Тестирование
    - Обнаружен переход в вечный цикл при некоторых запусках.
    - Диагностика. Обнаружено, что пробелема проявляется при угадывании числа 1. Выявлена причина.
    - Исправление
3. Подготовка readme.
4. Публикация проекта на Github

:arrow_up:[к оглавлению](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

## Результат
При всех произведенных тестовых запусках, программа выдавала результат = 5 (среднее количество попыток, требуемых для поиска числа). Это лучше целевого значения (20) и близко к теоретически возможному лучшему среднему (4).

:arrow_up:[к оглавлению](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)

## Выводы
Цель проекта достигнута - навык написания хорошего кода на Phyton улучшен.

:arrow_up:[к оглавлению](https://github.com/SurenAleksanian/SF_DS_course/blob/main/project_0/readme.md#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
