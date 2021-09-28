import pytest
from fizz_buzz import FizzBuzz

@pytest.fixture
def fizz_buzz():
 return FizzBuzz()