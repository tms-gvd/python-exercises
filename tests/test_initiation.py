from exercises.initiation import mult_two
import pytest

def test_mult_two():
    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0