import pytest
from src.tw_validation_python.NationalIdentityNumberValidator import ValidIDNumber


@pytest.mark.parametrize(
    "id_number, expected",
    [
        ("A123456789", True),
        ("B234567890", False),
        ("C123456789", False),
        ("A12345678", False),
        ("a123456789", False),
        ("A323456789", False),
        ("A12a456789", False),
        ("", False),
        (None, False),
        ("Z123456789", False),
        ("O123456789", False),
    ],
)
def test_valid_id_number(id_number, expected):
    assert ValidIDNumber(id_number) == expected
