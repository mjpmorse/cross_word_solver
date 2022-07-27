from typing import List
import numpy as np
from solver.book import Book

def solver(
    M: np.array,
    word_list: List[str]
) -> List[Book]:

    book_list = []
    for iy, ix in np.ndindex(M.shape):
        h_fwd = ''.join([str(x) for x in M[ix, iy:]])
        h_fwd = h_fwd.upper()
        # +1 here since we want end point
        h_bck = ''.join(
            [str(x) for x in M[ix, :iy + 1][::-1]]
        )
        h_bck = h_bck.upper()
        v_fwd = ''.join([str(x) for x in M[ix:, iy]])
        v_fwd = v_fwd.upper()
        # +1 here since we want end point
        v_bck = ''.join(
            [str(x) for x in M[:ix + 1, iy][::-1]]
        )
        v_bck = v_bck.upper()
        # we could do this without making the submatrix,
        # but the upper and lower submatrix will make this
        # step cleaner and easier to read
        # reverse the upper matrix so we can use diagonal
        upperM = M[:ix + 1, :iy + 1][::-1, ::-1]
        lowerM = M[ix:, iy:]
        # now we grab the diagonals.
        d_fwd = ''.join([str(x) for x in np.diagonal(lowerM)])
        d_bck = ''.join([str(x) for x in np.diagonal(upperM)])
        d_fwd = d_fwd.upper()
        d_bck = d_bck.upper()

        # also need anti-diagonal
        lowerMad = M[ix:, :iy + 1][:, ::-1]
        upperMad = M[:ix + 1, iy:][::-1, :]
        ad_bck = ''.join([str(x) for x in np.diagonal(lowerMad)])
        ad_fwd = ''.join([str(x) for x in np.diagonal(upperMad)])
        ad_bck = ad_bck.upper()
        ad_fwd = ad_fwd.upper()
        for _word in word_list:
            word = _word.upper()
            if h_fwd.startswith(word):
                book_list.append(
                    Book(
                        word,
                        ix,
                        iy,
                        'horizontal forward'
                    )
                )
            if h_bck.startswith(word):
                book_list.append(
                    Book(
                        word,
                        ix,
                        iy,
                        'horizontal backward'
                    )
                )
            if v_fwd.startswith(word):
                book_list.append(
                    Book(
                        word,
                        ix,
                        iy,
                        'vertical forward'
                    )
                )
            if v_bck.startswith(word):
                book_list.append(
                    Book(
                        word,
                        ix,
                        iy,
                        'vertical backward'
                    )
                )

            if d_fwd.startswith(word):
                book_list.append(
                    Book(
                        word,
                        ix,
                        iy,
                        'diagonal forward'
                    )
                )
            if d_bck.startswith(word):
                book_list.append(
                    Book(
                        word,
                        ix,
                        iy,
                        'diagonal backward'
                    )
                )
            if ad_fwd.startswith(word):
                book_list.append(
                    Book(
                        word,
                        ix,
                        iy,
                        'anti-diagonal forward'
                    )
                )
            if ad_bck.startswith(word):
                book_list.append(
                    Book(
                        word,
                        ix,
                        iy,
                        'anti-diagonal backward'
                    )
                )
    return book_list


def remove_substring(book_list: List[Book]) -> List[Book]:
    """remove a word from the list if it is a substring
    of another word in the list.

    Args:
        answers (List[Book]): _description_
    """
    for book1 in book_list:
        for book2 in book_list:
            if (
                (book2.name in book1.name) and
                (book2.direction == book1.direction)
            ):
                book_list.remove(book2)

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
                # start is now the end, so add length of the word
                ix = row.find(word) + len(row)
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="horizontal backward"
                )
                book_list.append(book)
        for ix, col in enumerate(v_fwd):
            if word in col:
                iy = row.find(word)
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
                iy = row.find(word) + len(word)
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
                iy = min(offset, 0) + init
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
                ix = max(offset, 0) + init + len(word)
                iy = min(offset, 0) + init + len(word)
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
                # because we are going anti-diagonal we reverse x
                ix = len(M) - ix
                iy = min(offset, 0) + init
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
                ix = max(offset, 0) + init + len(word)
                ix = len(M) - ix
                iy = min(offset, 0) + init + len(word)
                book = Book(
                    name=word,
                    x=ix,
                    y=iy,
                    direction="anti-diagonal backward"
                )
                book_list.append(book)

    return book_list
