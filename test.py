import os

def test_installation():
    result = os.system("CS148 --help")
    assert(result == 0)