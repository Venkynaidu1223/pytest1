from venky import add,div
import pytest
def test_add():
    assert add(7,9)==16
    assert add(7,0)==7
    assert add(0,0)==0
def test_div():
    with pytest.raises(ValueError,match="any number can't divided by zero"):
        div(9,0)
        div(8,0)
    assert div(8,4)==2
    assert div(10,2)==5