import pytest
import numeric_input


def test_read_int(monkeypatch, capsys):
    inputs = iter([1,2])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    numeric_input.read_int("Skibidi Eingabe:",2,3)
    captured = capsys.readouterr().out
    assert captured == "Eingabe ist zu gross oder zu klein\n"

def test_invalid_value(monkeypatch, capsys):
    inputs = iter(["asdas", 2.0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    numeric_input.read_int("Skibidi Eingabe:", 2.0, 3.0)
    captured = capsys.readouterr().out
    assert captured == "Geben Sie eine Ganzzahl ein\n"

def test_read_float(monkeypatch, capsys):
    inputs = iter([1.0,2.0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    numeric_input.read_float("Skibidi Eingabe:",2.0,3.0)
    captured = capsys.readouterr().out
    assert captured == "Eingabe ist zu gross oder zu klein\n"

def test_invalid_value_float(monkeypatch, capsys):
    inputs = iter(["asdas", 2.0])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    numeric_input.read_float("Skibidi Eingabe:", 2.0, 3.0)
    captured = capsys.readouterr().out
    assert captured == "Geben Sie eine Zahl ein\n"