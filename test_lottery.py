import pytest
import lottery
from person import Person
from ticket import Ticket


def test_create_ticket(capsys, monkeypatch):
    inputs = iter([20, 15, 6, 3, 4, 2, 1])
    person = Person('Inga', 'geheim', 14.00)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    lottery.create_ticket(person)

    assert capsys.readouterr().out == (
    "   1   X   X   X   5   X\n"
    "   7   8   9  10  11  12\n"
    "  13  14   X  16  17  18\n"
    "  19   X  21  22  23  24\n"
    "  25  26  27  28  29  30\n"
    "  31  32  33  34  35  36\n"
    "  37  38  39  40  41\n"
    "\n"
    "Jokerzahl:  1\n"
    f"Dein neues Guthaben: {person.balance:.2f}\n"
)


def test_select_numbers_fail(capsys,monkeypatch):
    person = Person('Inga', 'geheim', 0.00)

    lottery.create_ticket(person)
    assert capsys.readouterr().out == "Zuwenig Guthaben\n"

def test_fail_create_ticket(capsys,monkeypatch):
    inputs = iter([20, 15, 6, 6, 3, 4, 2, 1])
    ticket = Ticket(0, list())
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    lottery.select_numbers(ticket)
    assert capsys.readouterr().out == "Diese Zahl haben Sie schon gewählt\n"