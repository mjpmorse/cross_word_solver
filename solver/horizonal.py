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
        # +1 here since we want end point
        h_bck = ''.join(
            [str(x) for x in M[ix, :iy + 1][::-1]]
        )
        v_fwd = ''.join([str(x) for x in M[ix:, iy]])
        # +1 here since we want end point
        v_bck = ''.join(
            [str(x) for x in M[:ix + 1, iy][::-1]]
        )
        # we could do this without making the submatrix,
        # but the upper and lower submatrix will make this
        # step cleaner and easier to read
        # reverse the upper matrix so we can use diagonal
        upperM = M[:ix + 1, :iy + 1][::-1, ::-1]
        lowerM = M[ix:, iy:]
        # now we grab the diagonals.
        d_fwd = ''.join([x for x in np.diagonal(lowerM)])
        d_bck = ''.join([x for x in np.diagonal(upperM)])
        for word in word_list:
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
    return book_list  
