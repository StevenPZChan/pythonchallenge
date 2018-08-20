import itertools

import numpy
from PIL import Image


class NonogramSolver:
    def __init__(self, dimension, horizontal, vertical):
        assert len(dimension) == 2
        self.rows, self.cols = dimension
        assert isinstance(self.rows, int) and isinstance(self.cols, int)
        assert self.rows == len(horizontal) and self.cols == len(vertical)
        self.horizontal = horizontal
        self.vertical = vertical
        self._row_solved = [0] * self.rows
        self._col_solved = [0] * self.cols

    def solve(self):
        self._initial()
        changed = True
        while changed:
            changed = self._update_scanner()

    @property
    def solution(self):
        result = Image.new('L', (self.rows, self.cols))
        for x, y in itertools.product(range(result.width), range(result.height)):
            result.putpixel((x, y), 255 * int(self._solution[y, x]))
        return result

    def _initial(self):
        self._row_possible = [self._get_all_situations(self.rows, dist) for dist in self.horizontal]
        self._col_possible = [self._get_all_situations(self.cols, dist) for dist in self.vertical]
        self._solution = 9 * numpy.ones((self.rows, self.cols), int)

    def _solve_single_line(self, before, possible):
        filtered = [p for p in possible if self._check_correctness(p, before)]
        solved = self._merge_situation(filtered)
        return numpy.array(list(int(s) for s in solved)), filtered

    def _solve_single_row(self, row):
        temps, self._row_possible[row] = self._solve_single_line(self._solution[row], self._row_possible[row])
        if len(self._row_possible[row]) == 1:
            self._row_solved[row] = True
        if str(temps) != str(self._solution[row]):
            self._solution[row] = temps
            return True
        return False

    def _solve_single_col(self, col):
        temps, self._col_possible[col] = self._solve_single_line(self._solution[:, col], self._col_possible[col])
        if len(self._col_possible[col]) == 1:
            self._col_solved[col] = True
        if str(temps) != str(self._solution[:, col]):
            self._solution[:, col] = temps
            return True
        return False

    @staticmethod
    def _check_correctness(possible, now):
        for i in range(len(now)):
            if now[i] != 9 and now[i] != int(possible[i]):
                return False
        return True

    def _get_all_situations(self, num, dist):
        if num < sum(dist) + len(dist) - 1:
            return None
        if not dist:
            return ['0' * num]

        all_sit = []
        sit0 = self._get_all_situations(num - 1, dist)
        if sit0:
            all_sit.extend('0' + s for s in sit0)
        if len(dist) == 1:
            all_sit.extend('1' * dist[0] + s for s in self._get_all_situations(num - dist[0], dist[1:]))
        else:
            all_sit.extend('1' * dist[0] + '0' + s for s in self._get_all_situations(num - dist[0] - 1, dist[1:]))
        return all_sit

    @staticmethod
    def _merge_situation(sits):
        result = ''
        for i in range(len(sits[0])):
            temp = sum(int(s[i]) for s in sits)
            if temp == len(sits):
                result += '1'
            elif temp == 0:
                result += '0'
            else:
                result += '9'
        return result

    def _update_scanner(self):
        changed = False
        for r in range(self.rows):
            if self._row_solved[r]:
                continue
            changed = self._solve_single_row(r) or changed
        for c in range(self.cols):
            if self._col_solved[c]:
                continue
            changed = self._solve_single_col(c) or changed
        return changed
