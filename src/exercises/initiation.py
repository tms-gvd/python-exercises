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
        data (list): list to check

    Returns:
        list: list consisting of only the non-unique elements in the input list. 
    """
    return [val for val in data if data.count(val)>1]