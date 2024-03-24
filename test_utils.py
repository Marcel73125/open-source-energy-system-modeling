from utils import glucoselevel

def test_glucoselevel():
    
    assert glucoselevel(80, 0) == 80
    assert glucoselevel(-1, 1) == -1
