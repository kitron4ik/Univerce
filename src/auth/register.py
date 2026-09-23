"""Модуль регистрации пользователя."""


def register(username: str, password: str) -> dict:
    """Создаёт учётную запись пользователя."""
    return {"username": username, "active": True}
