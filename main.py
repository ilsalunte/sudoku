from constants import BOARD
from actions import validate_inputted_data, WrongInput, put_number_on_board, is_sudoku_solved, is_sudoku_filled, \
     format_field


def main() -> None:
    print_board()

    while True:
        print('Podaj dane potrzebne do uzupełnienia liczby w kolejności: wiersz, '
              'kolumna, liczba. Nie używaj spacji ani przecinków.')
        inputted_data = input()
        try:
            validated_data = validate_inputted_data(inputted_data)
            put_number_on_board(validated_data)

        except WrongInput as ex:
            print(f'Wystąpił błąd: {ex}')

        print_board()

        if is_sudoku_filled():
            if is_sudoku_solved():
                print('Gratulacje!')
                break
            print('Sudoku nie jest uzupełnione prawidłowo.')


def print_board() -> None:
    print('    A B C | D E F | G H I')
    for i in range(9):
        row = [format_field(BOARD, i, x) for x in range(9)]
        print(f'{i + 1} | {row[0]} {row[1]} {row[2]} | {row[3]} '
              f'{row[4]} {row[5]} | {row[6]} {row[7]} {row[8]} |')
        if i in (2, 5):
            print('  |-----------------------|')


if __name__ == '__main__':
    main()
