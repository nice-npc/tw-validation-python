letters = "ABCDEFGHJKLMNPQRSTUVXYWZIO"


def ValidIDNumber(idNumber: str) -> bool:
    if idNumber is None or len(idNumber) != 10:
        return False
    if not (idNumber[0].isupper() and idNumber[0].isalpha()):
        return False
    if idNumber[1] not in {"1", "2"}:
        return False
    if not idNumber[2:].isdigit():
        return False

    letter_value = letters.index(idNumber[0]) + 10

    sum_digits = letter_value // 10 + (letter_value % 10) * 9

    for i in range(1, 9):
        sum_digits += int(idNumber[i]) * (9 - i)

    check_digit = (10 - sum_digits % 10) % 10

    last_char = int(idNumber[9])
    return check_digit == last_char
