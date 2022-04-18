from collections.abc import MutableSequence
from typing import Any


def swap(seq: MutableSequence[Any], frst_idx: int, snd_idx: int) -> MutableSequence[Any]:
    """Swaps two elements in the `seq`."""
    if seq[frst_idx] == seq[snd_idx]:
        return seq
    seq[frst_idx], seq[snd_idx] = seq[snd_idx], seq[frst_idx]
    return seq


def selection_sort(seq: MutableSequence[Any]) -> MutableSequence[Any]:
    """Sorting by selection.

    Algorithm in-place, complexity: T(n) = O(n**2).
    """
    size: int = len(seq)
    for i in range(size):
        min_idx: int = -1
        for j in range(i, size):
            if min_idx == -1 or seq[j] < seq[min_idx]:
                min_idx = j
        swap(seq, min_idx, i)
    return seq


def insertion_sort(seq: MutableSequence[Any]) -> MutableSequence[Any]:
    """Sorting by inserts.

    Algorithm in-place, complexity: T(n) = O(n**2).
    """
    for i in range(len(seq)):
        j: int = i
        while j > 0 and seq[j - 1] > seq[j]:
            swap(seq, j-1, j)
            j -= 1
    return seq


def replace_subseq(
        seq: MutableSequence[Any],
        begin_subseq: int,
        end_subseq: int,
        tmp_seq: MutableSequence[Any]) -> None:
    """Replaces a subsequence in the `seq` by elements from the beginning of the `tmp_seq`."""
    l_idx = begin_subseq
    for i in range(end_subseq - begin_subseq + 1):
        assert l_idx <= end_subseq
        seq[l_idx] = tmp_seq[i]
        l_idx += 1


def merge_sorted_seqs(
        seq: MutableSequence[Any],
        tmp_seq: MutableSequence[Any],
        l_begin_seq: int,
        l_end_seq: int,
        r_begin_seq: int,
        r_end_seq: int) -> None:
    """Merges two sorted seqs in ascending order."""
    l_seq_idx: int = l_begin_seq
    r_seq_idx: int = r_begin_seq
    l_seq_len: int = l_end_seq - l_begin_seq + 1
    r_seq_len: int = r_end_seq - r_begin_seq + 1
    tmp_seq_idx = 0

    while l_seq_idx - l_begin_seq < l_seq_len and r_seq_idx - r_begin_seq < r_seq_len:
        if seq[l_seq_idx] <= seq[r_seq_idx]:
            tmp_seq[tmp_seq_idx] = seq[l_seq_idx]
            tmp_seq_idx += 1
            l_seq_idx += 1
        else:
            tmp_seq[tmp_seq_idx] = seq[r_seq_idx]
            tmp_seq_idx += 1
            r_seq_idx += 1
    while l_seq_idx - l_begin_seq < l_seq_len:
        tmp_seq[tmp_seq_idx] = seq[l_seq_idx]
        tmp_seq_idx += 1
        l_seq_idx += 1
    while r_seq_idx - r_begin_seq < r_seq_len:
        tmp_seq[tmp_seq_idx] = seq[r_seq_idx]
        tmp_seq_idx += 1
        r_seq_idx += 1

    replace_subseq(seq, l_begin_seq, r_end_seq, tmp_seq)


def merge_sort(seq: MutableSequence[Any]) -> MutableSequence[Any]:
    """Mergesort.

    This algorithm has complexity O(n*log(n)).
    """
    size = len(seq)
    tmp_seq = [None for _ in range(size)]
    if size == 0:
        return seq

    def _merge_sort(_seq: MutableSequence[Any], begin: int, end: int) -> MutableSequence[Any]:
        delimetr_idx = (end - begin) // 2
        l_seq_begin = begin
        l_seq_end = l_seq_begin + delimetr_idx
        r_seq_begin = l_seq_end + 1
        r_seq_end = end

        if r_seq_end - l_seq_begin == 0:
            return _seq
        # sort left subseq
        _merge_sort(_seq, begin=l_seq_begin, end=l_seq_end)
        # sort right subseq
        _merge_sort(_seq, begin=r_seq_begin, end=r_seq_end)
        # merge left and right subseqs
        merge_sorted_seqs(seq, tmp_seq, l_seq_begin, l_seq_end, r_seq_begin, r_seq_end)
        return _seq
    return _merge_sort(seq, 0, size - 1)


def partition(seq: MutableSequence[Any], l_idx: int, r_idx: int) -> int:
    """Rearranges the `seq` around the pivot.

    Rearranges the sequence such that all elements that are less than or equal to the pivot have
    smaller indices than the pivot,
    and all elements that are greater than the pivot have higher indices than the pivot.
    Without loss of generality the pivot is taken as the `l_idx`-th element of the `seq`.
    """
    pivot_idx = l_idx
    i = l_idx + 1
    j = r_idx
    while i != j:
        if seq[i] > seq[pivot_idx]:
            swap(seq, i, j)
            j -= 1
        else:
            swap(seq, i, pivot_idx)
            pivot_idx = i
            i += 1
    if seq[pivot_idx] >= seq[i]:
        swap(seq, pivot_idx, i)
        pivot_idx = i
    return pivot_idx


def quick_sort(seq: MutableSequence[Any]) -> MutableSequence[Any]:
    """Quicksort or Hoare's sort.

    Algorithm in-place, complexity: O(n*log(n)) for a totally unsorted seq.
    """
    def _quick_sort(
            _seq: MutableSequence[Any],
            _begin: int,
            _end: int) -> MutableSequence[Any]:
        if _begin >= _end:
            return _seq
        pivot = partition(_seq, _begin, _end)
        _quick_sort(_seq, _begin, pivot - 1)
        _quick_sort(_seq, pivot + 1, _end)
        return _seq
    return _quick_sort(seq, 0, len(seq) - 1)
