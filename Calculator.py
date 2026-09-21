# calculator.py

def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    if not marks:
        raise ValueError("marks cannot be empty")
    return calculate_total(marks) / len(marks)


def get_result(marks):
    return "PASS" if calculate_average(marks) >= 40 else "FAIL"
