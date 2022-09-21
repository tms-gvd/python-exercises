from exercises.initiation import mult_two, checkio
import pytest

def test_mult_two():
    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0

def test_checkio():
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
    assert checkio([1, 2, 3, 4, 5]) == []
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
    assert checkio([2, 2, 3, 2, 2]) == [2, 2, 2, 2]
    assert checkio([10, 20, 30, 10]) == [10, 10]
    assert checkio([7]) == []
    assert checkio([0, 1, 2, 3, 4, 0, 1, 2, 4]) == [0, 1, 2, 4, 0, 1, 2, 4]
    assert checkio([99, 98, 99]) == [99, 99]
    assert checkio([0, 0, 0, 1, 1, 100]) == [0, 0, 0, 1, 1]
    assert checkio([0, 0, 0, -1, -1, 100]) == [0, 0, 0, -1, -1]