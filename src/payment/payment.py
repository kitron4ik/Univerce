"""Модуль обработки платежей."""


def pay(amount: float, currency: str = "RUB") -> dict:
    """Проводит платёж на указанную сумму."""
    return {"amount": amount, "currency": currency, "status": "ok"}
