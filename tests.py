import pytest
from typing import Iterator

from matrix import iterate_rows


matrix = [[1, 2, 3, 4], [6, 7, 8, 9], [4, 5, 6, 7]]


@pytest.mark.parametrize(
    "matrix, mask, result",
    [
        (matrix, [True, False, True], [2, 4, 4, 6]),
        (matrix, [False, False, False], []),
        (matrix, [True, False, False], [2, 4]),
    ],
)
def test_iterate_rows(matrix, mask, result):
    iterator = iterate_rows(matrix=matrix, mask=mask)
    assert isinstance(iterator, Iterator)
    assert list(iterator) == result


def test_docstring():
    assert iterate_rows.__doc__
