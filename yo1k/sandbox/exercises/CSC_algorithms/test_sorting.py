import itertools
from collections.abc import Sequence, MutableSequence
from typing import Any

import pytest

import yo1k.sandbox.exercises.CSC_algorithms.sorting as my_sort


@pytest.fixture
def arrays_set() -> Sequence[MutableSequence[Any]]:
    return (
            [1, 2, 5, 7, 3, 10, 4, -1, 5],
            [1, 2, 3, 2, 7, 8, 4, 5, 2],
            [1, -2, -3, -2, -7, -8, -4, -5, -2],
            [2, 2, 2, 2, 2],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, 3, 1, 2, 1, 2, 1],
            [-3, 1],
            [-1],
            [])


def test_swap() -> None:
    assert my_sort.swap([1, 2, 5, 7, 3, 10, 4, -1, 5], 2, 4) == [1, 2, 3, 7, 5, 10, 4, -1, 5]


def test_selection_sort(arrays_set: Sequence[MutableSequence[Any]]) -> None:
    for array in arrays_set:
        array1, array2 = itertools.tee(array)
        assert my_sort.selection_sort(list(array1)) == sorted(list(array2))


def test_insertion_sort(arrays_set: Sequence[MutableSequence[Any]]) -> None:
    for array in arrays_set:
        array1, array2 = itertools.tee(array)
        assert my_sort.insertion_sort(list(array1)) == sorted(list(array2))


def test_merge_sort(arrays_set: Sequence[MutableSequence[Any]]) -> None:
    for array in arrays_set:
        array1, array2 = itertools.tee(array)
        assert my_sort.merge_sort(list(array1)) == sorted(list(array2))


def test_quick_sort(arrays_set: Sequence[MutableSequence[Any]]) -> None:
    for array in arrays_set:
        array1, array2 = itertools.tee(array)
        assert my_sort.quick_sort(list(array1)) == sorted(list(array2))


if __name__ == "__main__":
    pytest.main()
