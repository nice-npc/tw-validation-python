import re


class NationalPhoneNumberValidator:
    REGEX = r"(\+886\d{9}|09\d{8})"
    PATTERN = re.compile(REGEX)

    @staticmethod
    def is_valid(national_phone_number: str):
        if national_phone_number is None:
            return False

        if not national_phone_number.strip():
            return False

        return bool(
            NationalPhoneNumberValidator.PATTERN.fullmatch(national_phone_number)
        )
