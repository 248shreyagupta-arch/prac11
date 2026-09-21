from calculator import calculate_total
from calculator import calculate_average
from calculator import get_result
def test_total():
    marks = [80, 70, 90]
    assert calculate_total(marks) == 240
def test_average():
    marks = [80, 70, 90]
    assert calculate_average(marks) == 80
def test_pass_result():
    marks = [80, 70, 90]
    assert get_result(marks) == "PASS"
def test_fail_result():
    marks = [30, 35, 25]
    assert get_result(marks) == "FAIL"
