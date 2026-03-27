"""
Тесты для решённых задач. Минимум 65 тестов.
Используется pytest. Тестируемые функции импортируются и вызываются напрямую.
"""

import math
import os
import tempfile
import random

import pytest

# --- Импорты тестируемых модулей ---
from fact import fact_it, fact_rec
from log_decorator import greeting_format
from my_sum import my_sum
from email_validation import fun, filter_mail
from circle_square_mk import circle_square_mk
from complex_numbers import Complex
from people_sort import name_format
from phone_number import sort_phone
from plane_angle import plane_angle, Point
from average_scores import compute_average_scores
from fibonacci import fibonacci, cube
from file_search import find_file, get_first_lines
from files_sort import list_files
from sum_and_sub import sum_and_sub
from show_employee import show_employee
from process_list import process_list, process_list_gen


# ============== fact ==============
@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (2, 2), (5, 120), (10, 3628800)])
def test_fact_it(n, expected):
    assert fact_it(n) == expected


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (5, 120)])
def test_fact_rec(n, expected):
    assert fact_rec(n) == expected


# ============== log_decorator ==============
@pytest.mark.parametrize("name, expected", [
    ("John", "Hello, John!"),
    ("", "Hello, !"),
    ("Alice", "Hello, Alice!"),
])
def test_greeting_format(name, expected):
    assert greeting_format(name) == expected


# ============== my_sum ==============
@pytest.mark.parametrize("args, expected", [
    ((1, 2, 3), 6),
    ((0,), 0),
    ((-1, 1), 0),
    ((1,), 1),
    ((10, 20, 30, 40), 100),
    ((-5, -3, 8), 0),
])
def test_my_sum(args, expected):
    assert my_sum(*[str(x) for x in args]) == expected


# ============== email_validation ==============
@pytest.mark.parametrize("email, expected", [
    ("user@domain.com", True),
    ("a@b.co", True),
    ("test_user@site.org", True),
    ("user-name@website.abc", True),
    ("invalid", False),
    ("no-at-sign.com", False),
    ("@domain.com", False),
    ("user@", False),
    ("user@domain", False),
    ("user@.com", False),
    ("user@domain.cccc", False),
    ("user@domain.c", True),
])
def test_email_fun(email, expected):
    assert fun(email) == expected


def test_filter_mail_empty():
    assert filter_mail([]) == []


def test_filter_mail_mixed():
    emails = ["invalid", "valid@domain.com", "also@site.org", "bad"]
    result = filter_mail(emails)
    assert set(result) == {"valid@domain.com", "also@site.org"}
    assert len(result) == 2


# ============== circle_square_mk ==============
def test_circle_square_mk_r1_n100():
    random.seed(42)
    result = circle_square_mk(1.0, 100)
    assert 2.5 < result < 4.0


def test_circle_square_mk_r1_n10000():
    random.seed(42)
    result = circle_square_mk(1.0, 10000)
    expected = math.pi
    assert abs(result - expected) < 0.2


def test_circle_square_mk_r2():
    random.seed(123)
    result = circle_square_mk(2.0, 1000)
    expected = math.pi * 4
    assert 8 < result < 16


def test_circle_square_mk_zero_radius():
    result = circle_square_mk(0, 100)
    assert result == 0


# ============== complex_numbers ==============
def test_complex_add():
    a, b = Complex(1, 2), Complex(3, 4)
    c = a + b
    assert c.real == 4 and c.imaginary == 6


def test_complex_sub():
    a, b = Complex(5, 5), Complex(2, 3)
    c = a - b
    assert c.real == 3 and c.imaginary == 2


def test_complex_mul():
    a, b = Complex(1, 2), Complex(3, 4)
    c = a * b
    assert abs(c.real - (-5)) < 1e-9 and abs(c.imaginary - 10) < 1e-9


def test_complex_div():
    a, b = Complex(1, 0), Complex(1, 0)
    c = a / b
    assert abs(c.real - 1) < 1e-9 and abs(c.imaginary) < 1e-9


def test_complex_mod():
    c = Complex(3, 4)
    m = c.mod()
    assert abs(m.real - 5) < 1e-9 and abs(m.imaginary) < 1e-9


def test_complex_str_positive():
    c = Complex(1.5, 2.5)
    s = str(c)
    assert "1.50" in s and "2.50" in s


def test_complex_str_real_only():
    c = Complex(3, 0)
    assert "0.00" in str(c)


def test_complex_str_imag_only():
    c = Complex(0, 1)
    assert "1.00" in str(c)


def test_complex_str_negative_imag():
    c = Complex(1, -1)
    s = str(c)
    assert "1.00" in s


def test_complex_zero():
    c = Complex(0, 0)
    assert str(c) == "0.00+0.00i"


# ============== people_sort ==============
def test_name_format_single():
    people = [["John", "Doe", "20", "M"]]
    result = list(name_format(people))
    assert result == ["Mr. John Doe"]


def test_name_format_female():
    people = [["Jane", "Smith", "25", "F"]]
    result = list(name_format(people))
    assert result == ["Ms. Jane Smith"]


def test_name_format_sorted_by_age():
    people = [["Old", "Man", "50", "M"], ["Young", "Girl", "10", "F"]]
    result = list(name_format(people))
    assert result[0] == "Ms. Young Girl" and result[1] == "Mr. Old Man"


def test_name_format_multiple():
    people = [["A", "B", "30", "M"], ["C", "D", "20", "F"]]
    result = list(name_format(people))
    assert len(result) == 2


# ============== phone_number ==============
def test_sort_phone_single():
    phones = ["+79161234567"]
    assert sort_phone(phones) == ["+7 (916) 123-45-67"]


def test_sort_phone_multiple():
    phones = ["+79161234567", "+79031234567"]
    result = sort_phone(phones)
    assert result == ["+7 (903) 123-45-67", "+7 (916) 123-45-67"]


def test_sort_phone_short():
    phones = ["9161234567"]
    assert sort_phone(phones) == ["+7 (916) 123-45-67"]


def test_sort_phone_empty():
    assert sort_phone([]) == []


# ============== plane_angle ==============
def test_plane_angle_orthogonal():
    # Точки, образующие две перпендикулярные плоскости (угол 90°)
    A, B, C, D = Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(1, 1, 1)
    angle = plane_angle(A, B, C, D)
    assert 85 < angle < 95


def test_plane_angle_small():
    # Почти параллельные плоскости — малый угол
    A, B, C, D = Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(0.1, 1, 0.01)
    angle = plane_angle(A, B, C, D)
    assert 0 <= angle < 30


def test_plane_angle_general():
    A, B, C, D = Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0), Point(0, 1, 1)
    angle = plane_angle(A, B, C, D)
    assert 0 <= angle <= 180


def test_plane_angle_degenerate_raises():
    # Коллинеарные точки — деление на ноль
    A, B, C, D = Point(0, 0, 0), Point(1, 0, 0), Point(2, 0, 0), Point(3, 0, 0)
    with pytest.raises(ZeroDivisionError):
        plane_angle(A, B, C, D)


# ============== average_scores ==============
def test_compute_average_scores_single():
    scores = [(10.0,), (20.0,), (30.0,)]
    assert compute_average_scores(scores) == (20.0,)


def test_compute_average_scores_two_students():
    scores = [(10.0, 20.0), (30.0, 40.0)]
    result = compute_average_scores(scores)
    assert result == (20.0, 30.0)


def test_compute_average_scores_single_student():
    scores = [(100.0,)]
    assert compute_average_scores(scores) == (100.0,)


def test_compute_average_scores_three_subjects():
    scores = [(1, 2, 3), (4, 5, 6)]
    result = compute_average_scores(scores)
    assert result == (2.5, 3.5, 4.5)


# ============== fibonacci ==============
def test_fibonacci_zero():
    assert fibonacci(0) == []


def test_fibonacci_one():
    assert fibonacci(1) == [0]


def test_fibonacci_five():
    assert fibonacci(5) == [0, 1, 1, 2, 3]


def test_fibonacci_ten():
    fib = fibonacci(10)
    assert fib[-1] == 34 and len(fib) == 10


def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(0) == 0


# ============== file_search ==============
def test_find_file_exists():
    start = os.path.dirname(os.path.abspath(__file__))
    found = find_file(start, "test.py")
    assert found is not None
    assert "test.py" in found


def test_find_file_not_exists():
    start = os.path.dirname(os.path.abspath(__file__))
    found = find_file(start, "nonexistent_file_xyz_12345.py")
    assert found is None


def test_get_first_lines():
    start = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(start, "test.py")
    if os.path.isfile(test_file):
        lines = get_first_lines(test_file, 3)
        assert len(lines) <= 3
        assert isinstance(lines, list)


def test_get_first_lines_short_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("line1\nline2\n")
        path = f.name
    try:
        lines = get_first_lines(path, 5)
        assert lines == ["line1", "line2"]
    finally:
        os.unlink(path)


# ============== files_sort ==============
def test_list_files_current_dir():
    path = os.path.dirname(os.path.abspath(__file__))
    result = list_files(path)
    assert result is not None
    assert isinstance(result, list)
    if "test.py" in os.listdir(path):
        assert "test.py" in result


def test_list_files_nonexistent():
    result = list_files("/nonexistent/path/xyz123")
    assert result is None


def test_list_files_file_not_dir():
    path = __file__
    result = list_files(path)
    assert result is None


def test_list_files_empty_dir():
    with tempfile.TemporaryDirectory() as d:
        result = list_files(d)
        assert result == []


# ============== sum_and_sub ==============
@pytest.mark.parametrize("a, b, expected_sum, expected_sub", [
    (1, 1, 2, 0),
    (5, 3, 8, 2),
    (0, 0, 0, 0),
    (-1, 1, 0, -2),
])
def test_sum_and_sub(a, b, expected_sum, expected_sub):
    s, d = sum_and_sub(a, b)
    assert s == expected_sum and d == expected_sub


# ============== show_employee ==============
def test_show_employee_default_salary():
    assert show_employee("Иван") == "Иван: 100000 р"


def test_show_employee_custom_salary():
    assert show_employee("Петр", 50000) == "Петр: 50000 р"


def test_show_employee_zero_salary():
    assert show_employee("Анна", 0) == "Анна: 0 р"


def test_show_employee_name_only():
    s = show_employee("Test")
    assert "Test" in s and "100000" in s


# ============== process_list ==============
def test_process_list_even():
    assert process_list([2, 4]) == [4, 16]


def test_process_list_odd():
    assert process_list([1, 3]) == [1, 27]


def test_process_list_mixed():
    assert process_list([1, 2, 3, 4]) == [1, 4, 27, 16]


def test_process_list_empty():
    assert process_list([]) == []


def test_process_list_gen():
    result = list(process_list_gen([2, 3]))
    assert result == [4, 27]
