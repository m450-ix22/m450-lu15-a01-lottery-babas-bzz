import pytest
import authenticate
from person import Person


@pytest.fixture
def load_people():
    return authenticate.load_people()

def test_load_people_init(load_people):
    assert authenticate.load_people() == load_people

def test_is_list(load_people):
    assert isinstance(load_people, list)

@pytest.mark.xfail
def test_append_wrong(load_people):
    load_people.append("asfasd")
    assert authenticate.load_people() == load_people

def test_return_person(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "geheim")
    result = authenticate.login()
    assert result == Person('Inga', 'geheim', 14.00)

def test_login_fail(capsys, monkeypatch):
    people = iter(["asdd", "geheim", KeyboardInterrupt])
    monkeypatch.setattr('builtins.input', lambda _: next(people))
    authenticate.login()
    caputured = capsys.readouterr().out
    assert caputured == f"Passwort falsch\nPasswort falsch\nPasswort falsch\n"

