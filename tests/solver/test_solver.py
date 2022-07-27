import numpy as np
import pytest

from solver.solver import solver, solver2
from solver.book import Book


word_list = [
    ('cat', 'VF'),
    ('dog', 'HB'),
    ('zoo', 'HF'),
    ('fly', 'ADF'),
    ('animal', 'ADF'),
    ('cactus', 'ADF'),
    ('welcome', 'VF'),
    ('feed', 'DF'),
    ('hat', "DB"),
    ('moon', "ADB"),
    ('make', "VB")
]

@pytest.fixture
def generate_grid():
    m = np.array([
        ['M', 'E', 'V', 'Y', 'T', 'C', 'N', 'H', 'E', 'T'],
        ['Z', 'N', 'F', 'C', 'A', 'F', 'M', 'T', 'G', 'Q'],
        ['G', 'O', 'D', 'C', 'W', 'Q', 'E', 'A', 'A', 'Z'],
        ['X', 'O', 'T', 'M', 'E', 'X', 'N', 'E', 'F', 'H'],
        ['R', 'U', 'W', 'A', 'L', 'B', 'F', 'L', 'D', 'A'],
        ['S', 'C', 'G', 'K', 'C', 'N', 'E', 'S', 'N', 'F'],
        ['P', 'A', 'Z', 'O', 'O', 'U', 'G', 'I', 'L', 'E'],
        ['S', 'T', 'O', 'O', 'M', 'T', 'M', 'Y', 'E', 'K'],
        ['Z', 'M', 'M', 'D', 'E', 'A', 'D', 'Q', 'K', 'A'],
        ['M', 'S', 'K', 'U', 'L', 'T', 'Y', 'J', 'L', 'M']
    ])
    return m


@pytest.fixture
def load_dictionary():
    try:
        with open('/usr/share/dict/words', 'r') as f:
            all_words = f.read().split('\n')
    except FileExistsError:
        with open('./sample_dict.txt', 'r') as f:
            all_words = f.read().split('\n')

    all_words = [x.upper() for x in all_words]
    all_words = list(set(all_words))
    all_words = [x for x in all_words if len(x) >= 3]
    return all_words

@pytest.mark.parametrize("book", word_list)
def test_solver(
    generate_grid,
    load_dictionary,
    book
):
    m = generate_grid

    d = load_dictionary

    books = solver2(m, d)
    book_names = [book.name for book in books]
    assert book[0].upper() in book_names
