from collections.abc import MutableSequence
from typing import Any, Optional


def swap(array: MutableSequence[Any], frst_idx: int, snd_idx: int) -> MutableSequence[Any]:
    """Swaps to elements in a list."""
    array[frst_idx], array[snd_idx] = array[snd_idx], array[frst_idx]
    return array


def selection_sort(array: MutableSequence[Any]) -> MutableSequence[Any]:
    """Sorting by selection.

    Algorithm in-place, complexity: T(n) = O(n**2).
    """
    size: int = len(array)
    for i in range(size):
        min_idx: int = -1
        for j in range(i, size):
            if min_idx == -1 or array[j] <= array[min_idx]:
                min_idx = j
        swap(array, min_idx, i)
    return array


def insertion_sort(array: MutableSequence[Any]) -> MutableSequence[Any]:
    """Sorting by inserts.

    Algorithm in-place, complexity: T(n) = O(n**2).
    """
    for i in range(len(array)):
        j: int = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j-1, j)
            j -= 1
    return array


def merge_sorted_arrays(
        array_left: MutableSequence[Any],
        array_right: MutableSequence[Any],
        merged_array: Optional[MutableSequence[Any]] = None) -> MutableSequence[Any]:
    """Merges two sorted arrays in ascending order."""
    merged_array = [] if merged_array is None else merged_array
    l_idx: int = 0
    r_idx: int = 0
    l_end: int = len(array_left)
    r_end: int = len(array_right)

    while l_idx < l_end and r_idx < r_end:
        if array_left[l_idx] <= array_right[r_idx]:
            merged_array.append(array_left[l_idx])
            l_idx += 1
        else:
            merged_array.append(array_right[r_idx])
            r_idx += 1
    while l_idx < l_end:
        merged_array.append(array_left[l_idx])
        l_idx += 1
    while r_idx < r_end:
        merged_array.append(array_right[r_idx])
        r_idx += 1
    return merged_array


def merge_sort(array: MutableSequence[Any]) -> MutableSequence[Any]:
    """Mergesort.

    This algorithm has complexity O(n*log(n)) on condition
    when we do not take into account overheads of creating new arrays in the process of sorting,
    only comparison operation."""
    size: int = len(array)
    l_size: int = size // 2
    r_size: int = size // 2
    if size % 2 != 0:
        l_size += 1

    if r_size == 0:
        return array
    l_array = array[: l_size]
    r_array = array[l_size:]
    assert len(l_array) == l_size and len(r_array) == r_size
    l_array = merge_sort(l_array)
    r_array = merge_sort(r_array)
    sorted_array = merge_sorted_arrays(l_array, r_array)
    return sorted_array


def partition(array: MutableSequence[Any], l_idx: int, r_idx: int) -> int:
    """Changes `array` to: elements <= pivot, then a pivot element, elements > pivot.

    Without loss of generality the pivot is taken as the `l_idx`-th element of the `array`.
    """
    pivot_idx = l_idx
    i = l_idx + 1
    j = r_idx
    while i != j:
        if array[i] > array[pivot_idx]:
            swap(array, i, j)
            j -= 1
        else:
            swap(array, i, pivot_idx)
            pivot_idx = i
            i += 1
    if array[pivot_idx] >= array[i]:
        swap(array, pivot_idx, i)
        pivot_idx = i
    return pivot_idx


def quick_sort(
            array: MutableSequence[Any],
            begin: int = 0, end: Optional[int] = None) -> MutableSequence[Any]:
    """Quicksort or Hoare's sort.

    Algorithm in-place, complexity: O(n*log(n)) for totally unsorted an array.
    """
    if end is None:
        end = len(array) - 1

    def _quicksort(
            _array: MutableSequence[Any],
            _begin: int,
            _end: int) -> MutableSequence[Any]:
        if _begin >= _end:
            return _array
        pivot = partition(_array, _begin, _end)
        _quicksort(_array, _begin, pivot-1)
        _quicksort(_array, pivot+1, _end)
        return array
    return _quicksort(array, begin, end)
