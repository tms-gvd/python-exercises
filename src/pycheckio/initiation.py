from typing import Iterable
from datetime import datetime


def mult_two(int1: int, int2: int) -> int:
    """https://py.checkio.org/en/mission/multiply-intro/

    Args:
        input1 (int): first input
        input2 (int): second input

    Returns:
        int: multiplication of a and b.
    """
    return int1*int2


def checkio(data: list) -> list:
    """https://py.checkio.org/en/mission/non-unique-elements/

    Args:
        data (list): A list of integers.

    Returns:
        list: An iterable of integers, consisting of only the non-unique elements in the input list.
    """
    return [val for val in data if data.count(val)>1]


def flat_list(nested_list: list) -> list:
    """https://py.checkio.org/en/mission/flatten-list/

    Args:
        nested_list (list): A nested list with integers.

    Returns:
        list: The one-dimensional list with integers.
    """
    if len(nested_list)==0:
        return []
    if isinstance(nested_list[0], int):
        return [nested_list[0]] + flat_list(nested_list[1:])
    return flat_list(nested_list[0]) + flat_list(nested_list[1:])


def goes_after(word: str, first: str, second: str) -> bool:
    """https://py.checkio.org/en/mission/goes-after/

    Args:
        word (str): given string
        first (str): symbol that should go first
        second (str): symbol that should go right after the first one

    Returns:
        bool: the second symbol goes right after the first one
    """
    if first not in word:
        return False
    if first==second:
        return False
    ix_first = word.find(first)
    ix_second = word.find(second)
    return ix_second==ix_first+1 if ix_first<len(word)-1 else False


def split_pairs(text: str) -> Iterable[str]:
    """https://py.checkio.org/en/mission/split-pairs/

    Args:
        text (str): A string.

    Returns:
        Iterable[str]: A list or another Iterable of strings.
    """
    # if len(text)==0:
    #     return [""]
    if len(text)%2!=0:
        text += "_"
    for i in range(0, len(text), 2):
        yield text[i:i+2]


def is_all_upper(text: str) -> bool:
    """https://py.checkio.org/en/mission/all-upper/

    Args:
        text (str): A string.

    Returns:
        bool: all symbols are in upper case in the input.
    """
    return text.upper()==text


def frequency_sort(items: Iterable) -> Iterable:
    """https://py.checkio.org/en/mission/sort-array-by-element-frequency/

    Args:
        items (Iterable): Input iterable

    Returns:
        Iterable: Input sorted by the decreasing frequency of appearance of its elements
    """
    ix_count = {val: items.count(val) for val in items}
    interm = dict(sorted(ix_count.items(), key=lambda item: item[1], reverse=True))
    return [key for key, val in interm.items() for _ in range(val)]


def time_converter(time:str) -> str:
    """https://py.checkio.org/en/mission/time-converter-12h-to-24h/

    Args:
        time (str): Time in a 12-hour format

    Returns:
        str: Time in a 24-hour format
    """
    in_time = datetime.strptime(time.replace("p.m.", "PM").replace("a.m.", "AM"), "%I:%M %p")
    return datetime.strftime(in_time, "%H:%M")


def between_markers(text: str, begin: str, end: str) -> str:
    """https://py.checkio.org/en/mission/between-markers/

    Args:
        text (str): string to investigate
        begin (str): start marker
        end (str): end marker

    Returns:
        str: the substring of the input between the 2 markers
    """
    ix_begin, ix_end = text.find(begin), text.find(end)
    if ix_begin==-1 and ix_end==-1:
        return text
    if ix_begin==-1:
        return text[:ix_end]
    if ix_end==-1:
        return text[ix_begin+len(begin):]
    if ix_begin>ix_end:
        return ""
    return text[ix_begin+len(begin):ix_end]


def convert2roman(data:int) -> str:
    """https://py.checkio.org/en/mission/roman-numerals/

    Args:
        data (int): A number as an integer

    Returns:
        str: The Roman numeral as a string
    """
    result = ""
    chars = [("M", "", ""), ("C", "D", "M"), ("X", "L", "C"), ("I", "V", "X")]
    for char, roman_char in zip(str(data).zfill(4), chars):
        if int(char)<4:
            result += roman_char[0]*int(char)
        elif int(char)==4:
            result += roman_char[0]+roman_char[1]
        elif int(char)<9:
            result += roman_char[1]+roman_char[0]*(int(char)-5)
        else:
            result += roman_char[0]+roman_char[2]
    return result

if __name__=="__main__":
    pass
