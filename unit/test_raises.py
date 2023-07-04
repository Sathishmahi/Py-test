import pytest
from tuto_1.raise_test import validate_gender


def test_validate_gender():
    validate_gender("male")

def test_in_validate_gender():
    with pytest.raises(expected_exception=ValueError,match="gender must be male or female") as exc_info:
        validate_gender("mmale")
        # print(str(exc_info.value))
    