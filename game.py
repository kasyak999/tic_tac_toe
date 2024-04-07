"""Крестики нолики."""
from gameparts import Board, CellOccupiedError, FieldIndexError


def save_result(y_win):
    """ Сохранение результата игры в файл """
    with open('results.txt', 'a') as file:
        file.write(y_win + '\n')


def main():
    """ Сама прогрмма """
    game = Board()
    game.display()
    current_player = 'X'
    running = True

    while running:
        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                # field_size (это значение равно трём, оно хранится в модуле
                if row < 0 or row >= game.field_size + 1:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size + 1:
                    # ...выбросить исключение FieldIndexError.
                    raise FieldIndexError
                if game.board[row - 1][column - 1] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError
            except FieldIndexError as e:
                print(e)
                print(
                    'Значение должно быть неотрицательным и больше.'
                    f'{game.field_size + 1}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break
        game.make_move(row - 1, column - 1, current_player)
        print('Ход сделан!')
        game.display()
        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            result = f'Победил {current_player}!'
            save_result(result)
            print(result)
            running = False
        elif game.is_board_full():
            result = 'Ничья!'
            save_result(result)
            print(result)
            running = False
        current_player = 'O' if current_player == 'X' else 'X'  # Проверка игрока

    # ------------------------------------------
    # print(game)
    # print(type(game))
    # print(game.__class__)
    # print(isinstance(game, Board))
    # print(dir(game))
    # print('---------------')
    # print(game.__class__.__dict__)
    # #print(getsource(Board))
    # print('----------------')
    # print(Board.__doc__)


if __name__ == '__main__':
    main()
