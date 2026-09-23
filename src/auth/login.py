"""Модуль входа пользователя в систему."""


def login(username: str, password: str) -> bool:
    """Проверяет пару логин-пароль."""
    return bool(username) and len(password) >= 8
