"""Исключения"""


class FieldIndexError(IndexError):
    """Исключения для IndexError"""

    def __str__(self):
        return 'ОШИБКА: Введено значение за границами игрового поля'


class CellOccupiedError(ValueError):
    """ Искючения если поле занято другим игроком """

    def __str__(self):
        return 'Попытка изменить занятую ячейку'
