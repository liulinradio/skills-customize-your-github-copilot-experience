# 📘 Assignment: Your First Python Tests with pytest

## 🎯 Objective

Learn how automated tests check Python behavior by writing and running tests with pytest. Practice testing normal inputs and edge cases using clear assertions.

## 📝 Tasks

### 🛠️ Run the Starter Tests

#### Description
Install pytest and run the provided test file. The two tests will initially stop at TODO markers; replace those markers as you complete the tasks.

#### Requirements
Completed program should:

- Install pytest with `python -m pip install pytest`
- Run the tests from this assignment's folder with `python -m pytest -v`
- Confirm pytest discovers the tests in `test_starter_code.py`


### 🛠️ Test Even and Odd Numbers

#### Description
Complete `test_is_even()` with assertions that check the `is_even()` function using typical values and edge cases.

#### Requirements
Completed program should:

- Check that an even positive number returns `True`
- Check that an odd number returns `False`
- Include checks for zero and a negative number
- Use `assert` statements to compare each result with the expected value


### 🛠️ Test Addition Cases

#### Description
Complete `test_add_numbers()` with assertions that check addition for positive, zero, and negative values.

#### Requirements
Completed program should:

- Check the sum of two positive numbers
- Check adding zero
- Check adding a negative number
- Pass all tests when run with `python -m pytest -v`
