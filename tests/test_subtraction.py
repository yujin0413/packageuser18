
from packageuser18.subtraction import subtract

def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(1,1) == 0
    assert subtract(-1,-1) == 0
    assert subtract(0,1) == -1
