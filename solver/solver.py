from typing import List
import numpy as np
from solver.book import Book
from copy import deepcopy


def remove_substring(book_list: List[Book]) -> List[Book]:
    """remove a word from the list if it is a substring
    of another word in the list.

    Args:
        answers (List[Book]): _description_
    """
    tmp = [deepcopy(x) for x in book_list]
    for book1 in book_list:
        for book2 in book_list:
            if (
                (book2.name in book1.name) and
                (book2.direction == book1.direction)
            ):
                tmp.remove(book2)
                continue
    return tmp

def solver2(
    M: np.array,
    word_list: List[str]
) -> List[Book]:

    book_list = []

    # horizontal and vertical lists
    h_fwd = ["".join([str(z) for z in x]) for x in M]
    h_bck = [x[::-1] for x in h_fwd]

    v_fwd = ["".join([str(z) for z in x]) for x in M.T]
    v_bck = [x[::-1] for x in v_fwd]

    d_fwd = []
    d_bck = []
    ad_fwd = []
    ad_bck = []
    # diagonals we have to go over all offsets
    for offset in range(-1 * len(M) + 1, len(M)):
        tmp = np.diagonal(M, offset)
        # reverse columns to do anti-diagonal
        ad_tmp = np.diagonal(M[:, ::-1], offset)

        d_fwd.append(
            "".join([str(x) for x in tmp])
        )
        d_bck.append(
            "".join([str(x) for x in tmp[::-1]])
        )

        ad_fwd.append(
            "".join([str(x) for x in ad_tmp])
        )
        ad_bck.append(
            "".join([str(x) for x in ad_tmp[::-1]])
        )

    for word in word_list:
        # we are going to check each list now so we can
        # use different conditions to add starting position
        for iy, row in enumerate(h_fwd):
            if word in row:
                ix = row.find(word)
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="horizontal forward"
                )
                book_list.append(book)
        for iy, row in enumerate(h_bck):
            if word in row:
                # start is now the end, so we reverse
                ix = (len(M) - 1) - row.find(word)
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="horizontal backward"
                )
                book_list.append(book)
        for ix, col in enumerate(v_fwd):
            if word in col:
                iy = col.find(word)
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="vertical forward"
                )
                book_list.append(book)
        for ix, col in enumerate(v_bck):
            if word in col:
                # start is now end, so end is start
                iy = (len(M) - 1) - col.find(word)
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="vertical backward"
                )
                book_list.append(book)
        for _offset, diag in enumerate(d_fwd):
            offset = _offset - (len(M) - 1)
            if word in diag:
                init = diag.find(word)
                ix = max(offset, 0) + init
                iy = abs(min(offset, 0)) + init
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="diagonal forward"
                )
                book_list.append(book)
        for _offset, diag in enumerate(d_bck):
            offset = _offset - (len(M) - 1)
            if word in diag:
                init = diag.find(word)
                ix = max(offset, 0) + (len(diag) - init - 1)
                iy = abs(min(offset, 0)) + (len(diag) - init - 1)
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="diagonal backward"
                )
                book_list.append(book)
        for _offset, diag in enumerate(ad_fwd):
            offset = _offset - (len(M) - 1)
            if word in diag:
                init = diag.find(word)
                ix = max(offset, 0) + init
                ix = (len(M) - 1) - ix
                iy = abs(min(offset, 0)) + init
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="anti-diagonal forward"
                )
                book_list.append(book)
        for _offset, diag in enumerate(ad_bck):
            offset = _offset - (len(M) - 1)
            if word in diag:
                init = diag.find(word)
                ix = max(offset, 0) + (len(diag) - init - 1)
                ix = (len(M) - 1) - ix
                iy = abs(min(offset, 0)) + (len(diag) - init - 1)
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="anti-diagonal backward"
                )
                book_list.append(book)

    return book_list
