import numpy as np
import pytest

from solver.solver import solver, solver2
from solver.book import Book

word_list = [
    Book(name='cat', x=1, y=5, direction='vertical forward'),
    Book(name='dog', x=2, y=2, direction='horizontal backward'),
    Book(name='zoo', x=2, y=6, direction='horizontal forward'),
    Book(name='fly', x=9, y=5, direction='anti-diagonal forward'),
    Book(name='animal', x=9, y=4, direction='anti-diagonal forward'),
    Book(name='cactus', x=5, y=0, direction='anti-diagonal forward'),
    Book(name='welcome', x=4, y=2, direction='vertical forward'),
    Book(name='feed', x=5, y=1, direction='diagonal forward'),
    Book(name='hat', x=9, y=3, direction='diagonal backward'),
    Book(name='moon', x=2, y=8, direction='anti-diagonal backward'),
    Book(name='make', x=9, y=9, direction='vertical backward'),
    Book(name='rod', x=0, y=4, direction='anti-diagonal backward'),
    
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
    assert book in books
