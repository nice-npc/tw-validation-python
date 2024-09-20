import pytest
from src.tw_validation_python.MobileBarcodeValidator import (
    MobileBarcodeValidator,
)


@pytest.mark.parametrize(
    "mobile_barcode, expected",
    [
        ("/ABC1234", True),
        ("/A1B2C3D", True),
        ("/1234567", True),
        ("/ABC-123", True),
        ("/A.B+C-D", True),
        ("/123ABCD", True),
        ("ABC1234", False),
        ("/abc1234", False),
        ("/AB123", False),
        ("", False),
        (None, False),
        ("/ABC_123", False),
        ("/A1B2C3D4", False),
    ],
)
def test_is_valid(mobile_barcode, expected):
    assert MobileBarcodeValidator.is_valid(mobile_barcode) == expected
