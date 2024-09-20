import re


class MobileBarcodeValidator:
    REGEX = r"^/[A-Z0-9.\-+]{7}$"
    PATTERN = re.compile(REGEX)

    @staticmethod
    def is_valid(mobile_barcode: str):
        if mobile_barcode is None:
            return False
        return bool(MobileBarcodeValidator.PATTERN.fullmatch(mobile_barcode))
