BOARD = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 0],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]


COLUMN = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}

FORBIDDEN_FIELDS = {
        (0, 0), (0, 1), (0, 4), (1, 0), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 7), (3, 0), (3, 4),
        (3, 8), (4, 0), (4, 3), (4, 5), (4, 8), (5, 0), (5, 4), (5, 8), (6, 1), (6, 6), (6, 7), (7, 3),
        (7, 4), (7, 5), (7, 6), (8, 4), (8, 7), (8, 8)
    }
