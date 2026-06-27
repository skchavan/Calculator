import pytest
from calculator_logic import calculate 

def test_addition():
    # Fixed the smart quotes/typo "2+3′′" to standard quotes
    assert calculate("2+3") == 5

def test_subtraction():
    assert calculate("10-4") == 6

def test_multiplication():
    assert calculate("5*6") == 30

def test_division():
    assert calculate("20/5") == 4

def test_decimal():
    # Fixed the line break so the assertion comparison is valid
    assert calculate("2.5+1.5") == 4.0

def test_division_by_zero():
    assert calculate("5/0") == "Error: Division by Zero"

def test_invalid_expression():
    assert calculate("5++") == "Error"