import pytest
from src.tw_validation_python.IDNumber import ValidIDNumber
def test_FakeIdNumber() -> bool:
    assert ValidIDNumber("AA23456789") is False

def test_FakeGenderNumber() -> bool:
    assert ValidIDNumber("A323456789") is False

def test_WrongLengthNumber() -> bool:
    assert ValidIDNumber("AA") is False

def test_WrongFormatNumber() -> bool:
    assert ValidIDNumber("ABCDEFWF00") is False

def test_WrongCheckNumber1() -> bool:
    assert ValidIDNumber("A223456789") is False

def test_WrongCheckNumber2() -> bool:
    assert ValidIDNumber("A123456780") is False
    
def test_RealNumber() -> bool:
    assert ValidIDNumber("A123456789") is True
    
