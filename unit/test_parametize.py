import pytest
from tuto_1.parameterizing_marker import add

@pytest.mark.parametrize("a,b,c",[(1,2,3),("a","b","ab"),(1,0,1)]
,ids=["num","str","num"])
def test_parametrize_add(a,b,c):
    assert add(a,b) == c