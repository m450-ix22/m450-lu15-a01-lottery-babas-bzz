import pytest
import menu

def test_show_menu(capsys):
    menu.show_menu()
    assert capsys.readouterr().out == "Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n"

def test_select_menu(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "A")
    res = menu.select_menu()
    assert res == "A"

def test_select_menu_invalid(capsys, monkeypatch):
    inputs = iter(["E", "A"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    res = menu.select_menu()
    assert capsys.readouterr().out == "Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\nBitte geben Sie eine gültige Wahl ein\n"
    assert res == "A"
