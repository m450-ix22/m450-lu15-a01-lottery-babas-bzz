import pytest
import ticket

def test_value_error():
    with pytest.raises(ValueError):
        sigma = ticket.Ticket(2, list())
        sigma.joker = "asdd"
