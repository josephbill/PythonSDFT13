from calculator import add,substract,divide,multiply

def test_add():
    assert add(50,20) == 70

def test_subtract():
    assert substract(50,20) == 30
    
def test_multiply():
    assert multiply(50,20) == 1000
    
def test_divide():
    assert divide(50,20) == 2.5
