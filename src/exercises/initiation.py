import numpy as np

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

def flat_list(nested_list: list) -> list:
    """https://py.checkio.org/en/mission/flatten-list/

    Args:
        nested_list (list): A nested list with integers. 
    
    Returns:
        list: The one-dimensional list with integers. 
    """
    if len(nested_list)==0:
        return []
    elif isinstance(nested_list[0], int):
        return [nested_list[0]] + flat_list(nested_list[1:])
    else:
        return flat_list(nested_list[0]) + flat_list(nested_list[1:])