import numpy as np

from solver.solver import solver2
from solver.reconstruct import add_book

with open('/usr/share/dict/words', 'r') as f:
    all_words = f.read().split('\n')

all_words = [x.upper() for x in all_words]
all_words = list(set(all_words))
all_words = [x for x in all_words if len(x) > 4]

grid = np.loadtxt('./word_grid.txt', dtype=str)
grid = grid.reshape(-1, 1)
_grid = []
for idx in range(len(grid)):
    _grid.append(list(grid[idx].tolist()[0]))
del grid
_grid = np.array(_grid)
output = solver2(_grid, all_words)

result = np.array([[' '] * 50] * 50)
for book in output:
    result = add_book(result, book)

np.savetxt("solver_puzzle.csv", result, delimiter=",", fmt='%s')
