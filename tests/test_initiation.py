from exercises.initiation import *
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

def test_flat_list():
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"

def test_goes_after():
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False

def test_split_pairs():
    assert list(split_pairs("abcd")) == ["ab", "cd"]
    assert list(split_pairs("abc")) == ["ab", "c_"]
    assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
    assert list(split_pairs("a")) == ["a_"]
    assert list(split_pairs("")) == []

def test_is_all_upper():
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == True
    assert is_all_upper("444") == True
    assert is_all_upper("55 55 5 ") == True

def test_frequency_sort():
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]

def test_time_converter():
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'

def test_between_markers():
    assert between_markers("What is >apple<", ">", "<") == "apple"
    assert (
        between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
        == "My new site"
    )
    assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
    assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
    assert between_markers("No hi", "[b]", "[/b]") == "No hi"
    assert between_markers("No <hi>", ">", "<") == ""

def test_convert2roman():
    assert convert2roman(6) == 'VI', '6'
    assert convert2roman(76) == 'LXXVI', '76'
    assert convert2roman(499) == 'CDXCIX', '499'
    assert convert2roman(3888) == 'MMMDCCCLXXXVIII', '3888'