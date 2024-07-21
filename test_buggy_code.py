import pytest
from buggy_code import calculate_sum


def test_calculate_sum(capfd):
    numbers = [1, 2, 3, 4, 5]
    calculate_sum(numbers)
    out, err = capfd.readouterr()
    assert out.strip() == "The sum of the list is: 15"


if __name__ == "__main__":
    pytest.main()
