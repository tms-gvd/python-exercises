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