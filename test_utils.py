from utils import glucoselevel
from utils import printglucoselevel

def test_glucoselevel():
    
    assert glucoselevel(80, 0) == 80
    assert glucoselevel(-1, 1) == -1
    assert glucoselevel  (70,0) == 80

def test_printglucoselevel():
    assert printglucoselevel(80, 2) == 0
    assert printglucoselevel(80, -10) == -1
