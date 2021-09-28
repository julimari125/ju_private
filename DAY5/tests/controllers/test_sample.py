
def test_fizz_buzz(fizz_buzz): 
    for test_case in [
        {"input":1, "expected": 1},
        {"input":2, "expected": 2},
        {"input":3, "expected": 'Fizz'},
        {"input":6, "expected": 'Fizz'},
        {"input":5, "expected": 'Buzz'},
        {"input":10, "expected": 'Buzz'},
        {"input":15, "expected": 'FizzBuzz'},
        {"input":30, "expected": 'FizzBuzz'},
    ]:
        assert fizz_buzz.convert(test_case["input"]) == test_case["expected"]

    # assert fizz_buzz.convert(1) == 1
    # assert fizz_buzz.convert(3) == 'Fizz'
    # assert fizz_buzz.convert(1) == 1
    # assert fizz_buzz.convert(2) == 2
    # assert fizz_buzz.convert(3) == 'Fizz' 
    # assert fizz_buzz.convert(6) == 'Fizz' 
    # assert fizz_buzz.convert(5) == 'Fizz' 
    # assert fizz_buzz.convert(10) == 'Buzz' 
    # assert fizz_buzz.convert(15) == 'FizzBuzz' 
    # assert fizz_buzz.convert(30) == 'FizzBuzz'