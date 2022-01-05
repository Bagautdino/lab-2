# Лабораторная работа  №2

### Задание
Написать программу на Python, которая советует пользователю подходящие аниме с сайта Anime-Planet на основе ответов пользователя в опросе.

Программа должна обеспечивать:
* Диалоговый интерфейс с пользователем. Система последовательно узнает об интересующих жанрах, сезонах, студиях и т.д. (соответственно полям в csv файле). Например:
    ```python
    Какой жанр вас интересует?
    >>> Drama, Mecha, Sci Fi
    Вас интересует многосерийное аниме или полнометражное?
    >>> # если пустая строка, то  пользователю это не очень важно
    Какая максимальная длительность?
    >>> 1 час
    ...
    ```
* Поиск в файле `anime.csv` названий подходящих пользователю аниме
* Формирование отчета в виде файла

**Вход программы:**
Файл `anime.csv`

**Выход программы:**
Отчет в виде текстового файла
> **_ВАЖНО:_**
Результат оформить в виде репозитория на гитхабе.

> **_Дополнительно:_**
Для ТОП-5 аниме, полученных в результате поиска, скачать соответствующий постер с сайта Anime-Planet.
> За  выполнение +3 балла к лабе.
