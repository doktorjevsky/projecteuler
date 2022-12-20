"""
Given a set of triangles, determine how many of them contains the origin
"""


class Triangle:
    def __init__(self, p1, p2, p3):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._defined_set = (min(p1[0], p2[0], p3[0]), max(p1[0], p2[0], p3[0]))
        self._line_f_1 = LineFunction(p1, p2)
        self._line_f_2 = LineFunction(p1, p3)
        self._line_f_3 = LineFunction(p2, p3)

    def _is_defined(self, p):
        return self._defined_set[0] <= p[0] <= self._defined_set[1]

    def contains_point(self, p):
        if not self._is_defined(p):
            return False
        else:
            s = set()
            x = p[0]
            y = p[1]
            if self._line_f_1.is_defined(x):
                s.add(self._line_f_1.apply(x))
            if self._line_f_2.is_defined(x):
                s.add(self._line_f_2.apply(x))
            if self._line_f_3.is_defined(x):
                s.add(self._line_f_3.apply(x))

            y1 = min(s)
            y2 = max(s)
            return y1 <= p[1] <= y2


class LineFunction:
    def __init__(self, p1, p2):
        self._defined_set = (min(p1[0], p2[0]), max(p1[0], p2[0]))
        self._p1 = p1
        self._p2 = p2
        self._init_consts(p1, p2)
        self._m = p1[1] - self._k * p1[0]

    def _init_consts(self, p1, p2):
        if not p1[0] == p2[0]:
            self._k = (p1[1] - p2[1]) / (p1[0] - p2[0])
        else:
            self._k = 0 # eeeehhhh

    def is_defined(self, x):
        return self._defined_set[0] <= x <= self._defined_set[1]

    def apply(self, x):
        return self._k * x + self._m


def main():
    triangles = []
    with open("resources/in102.txt", "r") as f:
        for line in f:
            l = list(map(lambda x: int(x), line.split(",")))
            p1 = (l[0], l[1])
            p2 = (l[2], l[3])
            p3 = (l[4], l[5])
            t = Triangle(p1, p2, p3)
            triangles.append(t)

    res = sum(map(lambda t: 1 if t.contains_point((0, 0)) else 0, triangles))
    print(res)


if __name__ == '__main__':
    main()
