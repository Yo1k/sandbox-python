from collections.abc import MutableSequence


def my_pow(a: float, n: int) -> float:
    if n == 0:
        return 1
    b = my_pow(a, n//2)
    b = b * b
    if n % 2 == 1:
        b *= a
    return b


def my_fib(n: int) -> int:
    """ Give n-th fibonacci number.

    This recursive algorithm has complexity O(2^n)."""
    if n <= 1:
        return 1
    return my_fib(n-1) + my_fib(n-2)


def swap(frst_idx, snd_idx, array):
    array[frst_idx], array[snd_idx] = array[snd_idx], array[frst_idx]
    return array


def sort1(array):
    """ Sorting by choice.

    Complexity: O(n) <= T(n) <= O(n**2).
    """
    size = len(array)
    for i in range(size):
        min_idx = -1
        for j in range(i, size):
            if min_idx == -1 or array[j] <= array[min_idx]:
                min_idx = j
        swap(min_idx, i, array)
    return array


def sort2(array):  # SKTODO don't work
    """ Sorting by inserts."""
    for i in range(1, len(array)):
        j = i
        while j > 1 and array[j - 1] > array[j]:
            swap(j-1, j, array)
            j -= 1
    return array


def merge_sorted_array(array_left: MutableSequence, array_right: MutableSequence):
    """ Merges two sorted arrays in ascending order."""
    merged_array = []
    l_idx = 0
    r_idx = 0
    l_end = len(array_left)
    r_end = len(array_right)

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


def sort3(array):  # SKTODO change to use only one additional array
    """ Mergesort.

    This algorithm has complexity O(n*log(n)) on condition
    when we do not take into account overheads of creating new arrays in the sort process."""
    size = len(array)
    l_size = r_size = size // 2
    if size % 2 != 0:
        l_size += 1

    if r_size == 0:
        return array
    l_array = array[: l_size]
    r_array = array[l_size:]
    assert len(l_array) == l_size
    assert len(r_array) == r_size
    l_array = sort3(l_array)
    r_array = sort3(r_array)
    sorted_array = merge_sorted_array(l_array, r_array)
    return sorted_array


def array_border(array):
    """ Return indexes of the both array's ends when array: [l_idx, r_idx). """
    return 0, len(array)


def partition(array, l_idx, r_idx):
    """ Changes array to: elements <= x, then x element, elements > x.

    Initial array: [l_idx, r_idx], x - random element of the array put on position with l_idx."""
    pivot_idx = l_idx
    i = l_idx + 1
    j = r_idx
    while i != j:
        if array[i] > array[pivot_idx]:
            swap(i, j, array)
            j -= 1
        else:
            swap(i, pivot_idx, array)
            pivot_idx = i
            i += 1
    if array[pivot_idx] >= array[i]:
        swap(pivot_idx, i, array)
        pivot_idx = i
    return pivot_idx


def sort4(array, l_idx=0, r_idx=None):  # SKTODO finish function
    """ Quicksort or Hoare's sort.

    This algorithm has complexity O(n*log(n)) for totally unsorted an array. Works in place."""
    # l_idx0, r_idx0 = array_border(array)
    r_idx = len(array) - 1 if r_idx is None else r_idx
    if r_idx - l_idx == 0 or r_idx - l_idx == -1:
        return array
    pivot_idx = partition(array, l_idx, r_idx)
    sort4(array, l_idx, pivot_idx - 1)
    sort4(array, pivot_idx + 1, r_idx)
    return array


def partition2(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition2(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)


if __name__ == "__main__":
    assert my_pow(2, 9) == 512
    assert my_fib(5) == 8

    # my_array = [1, 2, 5, 7, 3, 10, 4, -1, 5]
    # assert swap(2, 4, my_array) == [1, 2, 3, 7, 5, 10, 4, -1, 5]
    # assert sort1(my_array) == [-1, 1, 2, 3, 4, 5, 5, 7, 10], f"my_array={my_array}"
    # assert sort2(my_array) == [-1, 1, 2, 3, 4, 5, 5, 7, 10], f"my_array={my_array}"
    #
    # a_l = [2, 3, 4, 8]
    # a_r = [1, 3, 5, 7]
    # ar = [1, 2, 3, 3, 4, 5, 7, 8]
    # assert merge_sorted_array(a_l, a_r) == [1, 2, 3, 3, 4, 5, 7, 8]
    # assert sort3(my_array) == [-1, 1, 2, 3, 4, 5, 5, 7, 10]
    # ar = [4, 3, 2, 8, 7, 1, -1, 5, 2]
    # ar2 = [1, 2, 3, 2, 7, 8, 4, 5, 2]
    # print(partition(ar, 0, 8))
    # print(partition([1, -1, 2, 2, 4, 3, 5, 7, 8], 0, 8))
    # print(partition(ar2, 0, 8))
    # print(partition(ar3, 0, 8))
    # print(sort4(ar))
    # print(sort4(ar2))
    # print(sort4(ar3))
    # print(sort4([-3, 1]))
    # ar3 = [1, -2, -3, -2, -7, -8, -4, -5, -2]
    #
    # print(quicksort(ar))
    # print(ar)
    # print(quicksort(ar2))
    # print(quicksort(ar3))
    # print(ar2)
    # print(ar3)
    # print(quicksort([-3, 1]))

