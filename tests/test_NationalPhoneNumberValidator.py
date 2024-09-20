import pytest
from src.tw_validation_python.NationalPhoneNumberValidator import (
    NationalPhoneNumberValidator,
)


@pytest.mark.parametrize(
    "national_phone_number, expected",
    [
        ("+886912345678", True),
        ("+886123456789", True),
        ("0912345678", True),
        ("091234567", False),
        ("+887123456789", False),
        ("+88691234567a", False),
        ("+886 912345678", False),
        ("", False),
        (None, False),
    ],
)
def test_is_valid(national_phone_number, expected):
    assert NationalPhoneNumberValidator.is_valid(national_phone_number) == expected
