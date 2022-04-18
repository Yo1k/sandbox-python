import copy
from collections.abc import Sequence, MutableSequence
from typing import Any

import pytest

import yo1k.sandbox.exercises.CSC_algorithms.sorting as my_sort


@pytest.fixture(name="lists_set")
def fixture_lists_set() -> Sequence[MutableSequence[Any]]:
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
            [],
            [[[1], [2]], [[1]], [[3]], [[1], [2]]],
            ["a", "c", "x", "b"])


def test_swap() -> None:
    assert my_sort.swap([1, 2, 5, 7, 3, 10, 4, -1, 5], 2, 4) == [1, 2, 3, 7, 5, 10, 4, -1, 5]


def test_selection_sort(lists_set: Sequence[MutableSequence[Any]]) -> None:
    for lst in lists_set:
        lst1, lst2 = lst, copy.copy(lst)
        assert my_sort.selection_sort(lst1) == sorted(lst2)


def test_insertion_sort(lists_set: Sequence[MutableSequence[Any]]) -> None:
    for lst in lists_set:
        lst1, lst2 = lst, copy.copy(lst)
        assert my_sort.insertion_sort(lst1) == sorted(lst2)


def test_merge_sort(lists_set: Sequence[MutableSequence[Any]]) -> None:
    for lst in lists_set:
        lst1, lst2 = lst, copy.copy(lst)
        assert my_sort.merge_sort(lst1) == sorted(lst2)


def test_quick_sort(lists_set: Sequence[MutableSequence[Any]]) -> None:
    for lst in lists_set:
        lst1, lst2 = lst, copy.copy(lst)
        assert my_sort.quick_sort(lst1) == sorted(lst2)


if __name__ == "__main__":
    pytest.main()
