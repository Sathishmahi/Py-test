import sys
import pytest
from tuto_1.marker_test import add,split_path


def test_add_normal():
    assert add(1,2) == 3

### to skip the unittest
@pytest.mark.skip(reason="i don't know")
def test_add_normal_skip():
    assert add(1,2) == 3

### to skip the unittest given condition
@pytest.mark.skipif(condition= sys.version_info <  (3,7), reason="python version is lower then 3.7")
def test_add_normal_skipif():
    assert add(1,2) == 3

### to ignore the exception statisfy given condtion
@pytest.mark.xfail(sys.platform == "win32")
def test_to_split_path():
    assert split_path(pa="C://Users//sathi//Postman") == ['C:', 'Users', 'sathi', 'Postman']
    # raise Exception("hello")