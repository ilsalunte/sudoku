from colorama import Fore, Style # type: ignore
from constants import BOARD, COLUMN, FORBIDDEN_FIELDS


class WrongInput(Exception):
    pass


def validate_inputted_data(data_str: str) -> tuple[int, str, int]:

    if len(data_str) != 3:
        raise WrongInput('Wprowadzono nieprawidłową ilość danych.')

    try:
        line = int(data_str[0])
        number = int(data_str[2])
    except ValueError:
        raise WrongInput('Wprowadzono nieprawidłowe dane wiersza lub liczbę.') from None

    if line not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or number not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        raise WrongInput('Wprowadzono nieprawidłowe dane wiersza lub liczbę.')

    column = data_str[1].upper()
    try:
        COLUMN[column]
    except KeyError:
        raise WrongInput('Wprowadzono nieprawidłową dane kolumny.') from None

    return line, column, number


def put_number_on_board(data: tuple[int, str, int]) -> None:

    if (data[0] - 1, COLUMN[data[1]]) in FORBIDDEN_FIELDS:
        raise WrongInput('Nie można zmienić podanego pola.')

    BOARD[data[0] - 1][COLUMN[data[1]]] = data[2]


def is_sudoku_filled() -> bool:
    for field in BOARD:
        if 0 in field:
            return False
    return True


def is_sudoku_solved() -> bool:
    for i in range(0, 8):
        numbers_line = provide_numbers_from_lines(i)
        numbers_column = provide_numbers_from_columns(i)
        numbers_square = provide_numbers_from_squares(i)

        if not all([len(numbers_line) == len(set(numbers_line))]) \
                or not all([len(numbers_column) == len(set(numbers_column))]) \
                or not all([len(numbers_square) == len(set(numbers_square))]):
            return False

    return True


def provide_numbers_from_lines(i: int) -> list[int]:
    return BOARD[i]


def provide_numbers_from_columns(i: int) -> list[int]:
    column = []
    for field in BOARD:
        column.append(field[i])
    return column


def provide_numbers_from_squares(i: int) -> list[int]:
    square = []
    start_row = (i // 3) * 3
    start_column = (i % 3) * 3
    square.extend(BOARD[start_row][start_column:(start_column + 3)])
    square.extend(BOARD[(start_row + 1)][start_column:(start_column + 3)])
    square.extend(BOARD[(start_row + 2)][start_column:(start_column + 3)])
    return square


def format_field(board: list[list[int]], line: int, field: int) -> str:
    if board[line][field] == 0:
        return ' '

    if (line, field) in FORBIDDEN_FIELDS:
        color = Fore.RED
    else:
        color = Fore.GREEN
    return color + str(board[line][field]) + Style.RESET_ALL



