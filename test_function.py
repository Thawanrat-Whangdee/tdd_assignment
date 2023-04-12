from function import validate_number,amount_of_vehicle
import pytest 

@pytest.mark.code #pytest => code
def test_people_morethan_11_divisible_by_4_input_15():
    input = 15
    excepted_result = "1 van 1 car"
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_morethan_11_divisible_by_4_input_19():
    input = 19
    excepted_result = "1 van 2 car"
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_morethan_11_not_divisible_by_4_input_12():
    input = 12
    excepted_result = "1 van 1 car" 
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_morethan_11_not_divisible_by_4_input_18():
    input = 18
    excepted_result = "1 van 2 car"
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_morethan_11_not_divisible_by_4_input_20():
    input = 20
    excepted_result = "1 van 3 car"
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_equal_11_input_11():
    input = 11
    excepted_result = "1 van 0 car"
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_lessthan_11_input_10():
    input = 10
    excepted_result = "1 van 0 car"
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_lessthan_11_input_1():
    input = 1
    excepted_result = "1 van 0 car"
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.code #pytest => code
def test_people_lessthan_11_input_5():
    input = 5
    excepted_result = "1 van 0 car"
    actual_result = amount_of_vehicle(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_amount_of_people_input_0():
    input = 0
    excepted_result = "input amount of people"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_amount_of_people_input_null():
    input = None
    excepted_result = "input amount of people"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_amount_of_people_input_0_5():
    input = 0.5
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_minus_1():
    input = -1
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_1_5():
    input = 1.5
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_minus_1_5():
    input = -1.5
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_char_a():
    input = "a"
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

@pytest.mark.validate #pytest => validate
def test_input_integer_input_char_sharp():
    input = "#"
    excepted_result = "input integer"
    actual_result = validate_number(input)
    assert excepted_result == actual_result

