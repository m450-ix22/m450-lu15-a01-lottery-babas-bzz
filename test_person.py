import pytest
import person

def test_value_error():
    with pytest.raises(ValueError) as exc_info:
        sigma = person.Person("herald", "skibidi", 12)
        sigma.balance = "asdd"
