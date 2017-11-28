import operator

class Solution:

    def island_perimeter(self, grid):
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
                   for row in grid + list(map(list, zip(*grid))))


