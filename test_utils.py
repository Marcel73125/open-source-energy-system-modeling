from utils import glucoselevel

def test_glucoselevel():
    from sympy import symbols, dsolve, Eq, Function
    from IPython.display import display
    
    assert glucoselevel(80, 0) == 80
    assert glucoselevel(80, 60) == 61.0704
    assert glucoselevel(-1, 1) == -1
