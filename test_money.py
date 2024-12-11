import pytest
from pylint.checkers.utils import builtins
import money
from person import Person


def test_transfer_E(monkeypatch):
    inputs = iter(["E", 25, "Z"])
    person = Person('Inga', 'geheim', 14)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    money.transfer_money(person)
    assert person.balance == 39.0

def test_transfer_A(monkeypatch):
    inputs = iter(["A", 25, "Z"])
    person = Person('Inga', 'geheim', 50)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    money.transfer_money(person)
    assert person.balance == 25.0


def test_transfer_A_invalid(monkeypatch):
    with pytest.raises(ValueError) as exc_info:
        inputs = iter(["A", 25, "Z"])
        person = Person('Inga', 'geheim', 0)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        money.transfer_money(person)
        assert exc_info.value == "Der Kontostand darf nicht unter 0 oder über 100 liegen"

def test_selection_invalid(capsys,monkeypatch):
    inputs = iter(["B", "A"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = money.select_transaction()
    assert capsys.readouterr().out == "Geben Sie eine gültige Auswahl ein\n"
    assert result == "A"
