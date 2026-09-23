"""Тесты модуля оплаты."""
from src.payment.payment import pay


def test_pay_returns_ok():
    assert pay(100.0)["status"] == "ok"
