"""Тесты модуля аутентификации."""
from src.auth.login import login


def test_login_short_password():
    assert login("user", "123") is False
