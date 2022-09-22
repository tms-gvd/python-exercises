from typing import Iterable
from datetime import datetime

def mult_two(a: int, b: int) -> int:
    """https://py.checkio.org/en/mission/multiply-intro/

    Args:
        a (int): first input
        b (int): second input

    Returns:
        int: multiplication of a and b.
    """
    return a*b


def checkio(data: list) -> list:
    """https://py.checkio.org/en/mission/non-unique-elements/

    Args:
        data (list): A list of integers. 

    Returns:
        list: An iterable of integers, consisting of only the non-unique elements in the input list. 
    """
    return [val for val in data if data.count(val)>1]


def flat_list(nl: list) -> list:
    """https://py.checkio.org/en/mission/flatten-list/

    Args:
        nl (list): A nested list with integers. 
    
    Returns:
        list: The one-dimensional list with integers. 
    """
    if len(nl)==0:
        return []
    elif isinstance(nl[0], int):
        return [nl[0]] + flat_list(nl[1:])
    else:
        return flat_list(nl[0]) + flat_list(nl[1:])


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
    elif first==second:
        return False
    else:
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
    elif ix_begin==-1:
        return text[:ix_end]
    elif ix_end==-1:
        return text[ix_begin+len(begin):]
    elif ix_begin>ix_end:
        return ""
    else:
        return text[ix_begin+len(begin):ix_end]