import pytest
from calculator import add

def test_add():   
    assert add(1,2) ==3
    assert add(3,4) ==7

def test_sub():
    assert sub(5,2) ==3
    assert sub(10,4) == 6
    assert sub(7,3) == 4

def test_mul():
    assert mul(2,3) == 6
    assert mul(4,5) == 24
    assert mul (3,3) == 10
    