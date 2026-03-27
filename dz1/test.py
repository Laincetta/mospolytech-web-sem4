import subprocess
import pytest
import tempfile
import os
from pathlib import Path

INTERPRETER = 'python3'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

def run_price_sum_with_file(file_content):
    """Функция для тестирования price_sum.py с разными файлами"""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.csv', delete=False) as f:
        f.write(file_content)
        temp_file = f.name
    
    try:
        original_dir = os.getcwd()
        with tempfile.TemporaryDirectory() as tmpdir:
            os.chdir(tmpdir)
            
            with open('products.csv', 'w', encoding='utf-8') as f:
                f.write(file_content)
            
            proc = subprocess.run(
                [INTERPRETER, os.path.join(original_dir, 'price_sum.py')],
                capture_output=True,
                text=True,
                check=False
            )
            os.chdir(original_dir)
            
        return proc.stdout.strip()
    finally:
        os.unlink(temp_file)

def run_script_with_workdir(script_path, workdir):
    """Функция для запуска скрипта в указанной рабочей директории"""
    proc = subprocess.run(
        [INTERPRETER, script_path],
        cwd=workdir,
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.stdout.strip().splitlines()

test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50'])
    ],
    'division': [
        (['4', '2'], ['2', '2.0']),
        (['10', '3'], ['3', '3.3333333333333335']),
        (['7', '5'], ['1', '1.4']),
        (['0', '5'], ['0', '0.0'])
    ],
    'loops': [
        (['3'], ['0', '1', '4']),
        (['5'], ['0', '1', '4', '9', '16']),
        (['1'], ['0']),
        (['0'], ['error'])
    ],
    'print_function': [
        (['3'], ['123']),
        (['5'], ['12345']),
        (['1'], ['1']),
    ],
    'second_score': [
        (['5', '10 8 7 6 5'], ['8']),
        (['3', '1 1 2'], ['1']),
        (['4', '10 9 9 8'], ['9'])
    ],
    'max_word': [
        ([], ['сосредоточенности']),
    ],
    'nested_list': [
        (['4', 'Alice', '50', 'Bob', '40', 'Charlie', '30', 'David', '20'], ['Charlie']),
        (['3', 'John', '85', 'Jane', '92', 'Jim', '78'], ['John']),
        (['4', 'Ann', '75', 'Beth', '74', 'Cate', '75', 'Dave', '90'], ['Ann', 'Cate']),
        (['5', 'Tom', '60', 'Jerry', '70', 'Spike', '60', 'Tyke', '80', 'Butch', '70'], ['Butch', 'Jerry'])
    ],
    'lists': [
        (['12', 'insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print'], 
         ['[6, 5, 10]', '[1, 5, 9, 10]', '[9, 5, 1]']),
        (['6', 'insert 0 3', 'insert 1 2', 'insert 2 1', 'print', 'reverse', 'print'], 
         ['[3, 2, 1]', '[1, 2, 3]']),
        (['5', 'append 5', 'append 3', 'append 8', 'sort', 'print'], 
         ['[3, 5, 8]'])
    ],
    'swap_case': [
        (['Hello World'], ['hELLO wORLD']),
        (['Pythonist 2'], ['pYTHONIST 2']),
        (['HackerRank.com presents "Pythonist 2".'], ['hACKERrANK.COM PRESENTS "pYTHONIST 2".']),
        (['123abc!@#'], ['123ABC!@#'])
    ],
    'split_and_join': [
        (['this is a string'], ['this-is-a-string']),
        (['Hello World Python'], ['Hello-World-Python']),
        (['one two three four'], ['one-two-three-four']),
        (['test'], ['test'])
    ],
    'price_sum': [
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
говядина,878.66,814.37,754.37
молоко,744.90,651.79,852.91
Фрукты свежие (Яблоки),588.45,441.34,1158.27
хлеб пшеничный,510.95,482.03,358.18
мясо птицы,502.28,482.96,428.87
творог,477.17,409.00,477.17
хлеб ржаной,426.09,216.45,155.84
рыба свежая,325.72,279.19,327.58
свинина,300.76,257.79,105.98
сыр,288.41,256.36,288.41
масло сливочное,232.62,211.48,387.70
Картофель,230.67,183.80,202.41
Яйца (штук),187.25,178.33,179.23
сахар,139.05,130.43,115.05
столовые корнеплоды,125.64,109.76,123.04
капуста свежая и квашеная,114.48,94.74,92.63
масло растительное,102.80,86.57,48.69
баранина,83.66,52.29,0.00
макаронные изделия,81.38,72.33,63.29
прочие овощи (морковь),78.14,69.15,76.41
огурцы и помидоры свежие и соленые,71.38,57.11,179.89
чай,51.22,51.22,40.97
сметана,46.54,46.54,69.82
другие крупы (кроме риса),40.77,37.06,44.48
конфеты,39.17,39.17,78.33
рис,31.23,31.23,41.64
маргарин и другие жиры,29.58,39.43,9.86
мука пшеничная,24.83,24.83,20.69
бобовые,21.88,18.23,10.94
специи,21.85,21.85,21.85
печенье,21.24,21.24,74.35
сельдь,18.33,18.33,18.33
соль,5.74,4.66,3.72""",
            "6842.84 5891.06 6810.90"
        ),
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
говядина,100.50,200.75,300.25""",
            "100.50 200.75 300.25"
        ),
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
товар1,10.50,20.75,30.25
товар2,40.25,50.50,60.75""",
            "50.75 71.25 91.00"
        ),
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
товар1,10.50,20.75,30.25
товар2,40.25,50.50,60.75
товар3,5.25,5.25,5.25
товар4,1.00,2.00,3.00""",
            "57.00 78.50 99.25"
        ),
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
товар1,0.00,0.00,0.00
товар2,0.00,0.00,0.00""",
            "0.00 0.00 0.00"
        ),
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
товар1,999.99,888.88,777.77
товар2,111.11,222.22,333.33""",
            "1111.10 1111.10 1111.10"
        ),
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
товар1,1.01,2.02,3.03
товар2,4.04,5.05,6.06
товар3,7.07,8.08,9.09""",
            "12.12 15.15 18.18"
        ),
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
яблоки,150.25,140.50,130.75
груши,120.50,110.25,100.00
бананы,80.75,70.50,60.25
апельсины,95.00,90.00,85.00
киви,45.25,40.25,35.25""",
            "491.75 451.50 411.25"
        ),
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
молоко,89.90,79.90,99.90
хлеб,45.50,40.50,35.50
яйца,120.00,110.00,100.00
сыр,250.00,240.00,230.00
масло,180.00,170.00,160.00""",
            "685.40 640.40 625.40"
        ),
        (
            """Продукт,Взрослый,Пенсионер,Ребенок
товар с длинным названием,123.45,234.56,345.67
еще один товар,456.78,567.89,678.90""",
            "580.23 802.45 1024.57"
        )
    ],
    'anagram': [
        (['listen', 'silent'], ['YES']),
        (['hello', 'world'], ['NO']),
        (['triangle', 'integral'], ['YES']),
        (['python', 'java'], ['NO'])
    ],
    'metro': [
        (['3', '1 5', '3 7', '6 9', '4'], ['2']),
        (['2', '10 20', '15 25', '15'], ['2']),
        (['4', '1 3', '4 6', '7 9', '10 12', '5'], ['1']),
        (['3', '1 10', '2 9', '3 8', '11'], ['0'])
    ],
    'minion_game': [
        (['BANANA'], ['Стюарт 12']),
        (['AAA'], ['Кевин 6']),
        (['BCDF'], ['Стюарт 10'])
    ],
    'is_leap': [
        (['2000'], ['True']),
        (['1900'], ['False']),
        (['2024'], ['True']),
        (['2023'], ['False'])
    ],
    'happiness': [
        (['5 3', '1 2 3 4 5', '1 3 5', '2 4'], ['1']),
        (['4 4', '1 2 3 4', '1 2', '3 4'], ['0']),
        (['3 2', '5 5 5', '5', '1 2'], ['3'])
    ],
    'pirate_ship': [
        (['10 3', 'Золото 4 100', 'Серебро 3 60', 'Бронза 5 50'], 
         ['Золото 4.00 100.00', 'Серебро 3.00 60.00', 'Бронза 3.00 30.00']),
        (['5 2', 'Алмазы 3 90', 'Изумруды 4 80'], 
         ['Алмазы 3.00 90.00', 'Изумруды 2.00 40.00']),
        (['15 3', 'Платина 5 200', 'Палладий 4 120', 'Родий 6 300'], 
         ['Родий 6.00 300.00', 'Платина 5.00 200.00', 'Палладий 4.00 120.00']),
        (['8 2', 'Медь 10 50', 'Никель 5 40'], 
         ['Никель 5.00 40.00', 'Медь 3.00 15.00'])
    ],
    'matrix_mult': [
        (['2', '1 2', '3 4', '5 6', '7 8'], 
         ['19 22', '43 50']),
        (['3', '1 0 0', '0 1 0', '0 0 1', '2 0 0', '0 2 0', '0 0 2'], 
         ['2 0 0', '0 2 0', '0 0 2']),
        (['2', '1 1', '1 1', '1 1', '1 1'], 
         ['2 2', '2 2']),
        (['2', '0 0', '0 0', '1 2', '3 4'], 
         ['0 0', '0 0'])
    ]
}

def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['max_word'])
def test_max_word(input_data, expected):
    assert run_script('max_word.py', input_data).split('\n') == expected

# Новые параметризованные тесты для max_word.py с файлами
@pytest.mark.parametrize(
    "file_text, expected",
    [
        # Пример с Обломовым
        (
            """В Гороховой улице, в одном из больших домов, народонаселения которого стало бы на
целый уездный город, лежал утром в постели.

Это был человек с отсутствием всякой сосредоточенности в чертах лица.
""",
            ["сосредоточенности"],
        ),
        # несколько слов одинаковой максимальной длины
        (
            "кот собака гиппопотам гиппопотам",
            ["гиппопотам", "гиппопотам"],
        ),
        # знаки препинания должны обрезаться
        (
            "hello!!! world??? Python...",
            ["Python"],
        ),
        # пустой файл
        (
            "",
            [],
        ),
        # один символ
        (
            "а б в г",
            ["а", "б", "в", "г"],
        ),
    ],
)
def test_max_word_files(tmp_path, file_text, expected):
    # создаём временную директорию
    script = Path(tmp_path) / "max_word.py"
    datafile = Path(tmp_path) / "example.txt"

    # копируем скрипт (предполагается, что он находится в текущей директории)
    script.write_text(Path("max_word.py").read_text(encoding="utf-8"), encoding="utf-8")

    # создаём тестовый файл
    datafile.write_text(file_text, encoding="utf-8")

    output = run_script_with_workdir(script.name, tmp_path)
    assert output == expected

# Тест для price_sum.py с разными файлами
@pytest.mark.parametrize("file_content, expected", test_data['price_sum'])
def test_price_sum(file_content, expected):
    result = run_price_sum_with_file(file_content)
    assert result == expected

@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected