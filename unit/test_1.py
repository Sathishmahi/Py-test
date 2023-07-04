from fun import add


### every pytest functuon and pytest file start with test_* and pytest class start with Test*

## test functions

def test_add_int():
    assert add(a=10, b=10) == 20

def test_add_str():
    assert add(a="10", b="10") == "1010"


### test classes

class TestAdd:
    def test_add_int(self):
        assert add(a=10, b=10) == 20

    def test_add_str(self):
        assert add(a="10", b="10") == "10110"