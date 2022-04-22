import copy
from collections.abc import Sequence, MutableSequence
from typing import Any

import pytest

import yo1k.sandbox.exercises.CSC_algorithms.sorting as my_sort


@pytest.fixture(name="seqs")
def fixture_seqs() -> Sequence[MutableSequence[Any]]:
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


def test_selection_sort(seqs: Sequence[MutableSequence[Any]]) -> None:
    for seq in seqs:
        seq1, seq2 = seq, copy.copy(seq)
        assert my_sort.selection_sort(seq1) == sorted(seq2)


def test_insertion_sort(seqs: Sequence[MutableSequence[Any]]) -> None:
    for seq in seqs:
        seq1, seq2 = seq, copy.copy(seq)
        assert my_sort.insertion_sort(seq1) == sorted(seq2)


def test_merge_sort(seqs: Sequence[MutableSequence[Any]]) -> None:
    for seq in seqs:
        seq1, seq2 = seq, copy.copy(seq)
        assert my_sort.merge_sort(seq1) == sorted(seq2)


def test_quick_sort(seqs: Sequence[MutableSequence[Any]]) -> None:
    for seq in seqs:
        seq1, seq2 = seq, copy.copy(seq)
        assert my_sort.quick_sort(seq1) == sorted(seq2)


if __name__ == "__main__":
    pytest.main()
