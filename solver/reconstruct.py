import numpy as np

from solver.book import Book


def add_book(
    M: np.array,
    B: Book
) -> np.array:
    title = B.name
    book_length = len(title)
    if B.direction == 'horizontal forward':
        for idx, letter in enumerate(title):
            M[B.y, B.x + idx] = letter

    if B.direction == 'horizontal backward':
        for idx, letter in enumerate(title):
            M[B.y, B.x - idx] = letter

    if B.direction == 'vertical forward':
        for idx, letter in enumerate(title):
            M[B.y + idx, B.x] = letter

    if B.direction == 'vertical backward':
        for idx, letter in enumerate(title):
            M[B.y - idx, B.x] = letter

    if B.direction == 'diagonal forward':
        for idx, letter in enumerate(title):
            M[B.y + idx, B.x + idx] = letter

    if B.direction == 'diagonal backward':
        for idx, letter in enumerate(title):
            M[B.y - idx, B.x - idx] = letter

    if B.direction == 'anti-diagonal forward':
        for idx, letter in enumerate(title):
            M[B.y + idx, B.x - idx] = letter

    if B.direction == 'anti-diagonal backward':
        for idx, letter in enumerate(title):
            M[B.y - idx, B.x + idx] = letter
    return M
