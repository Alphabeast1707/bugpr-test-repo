import pytest
from inventory import apply_discount, bulk_price


def test_discount_whole_cents() -> None:
    assert apply_discount(1000, 15) == 850


def test_discount_bounds() -> None:
    with pytest.raises(ValueError):
        apply_discount(100, 101)


def test_bulk_small_and_large() -> None:
    assert bulk_price(100, 2) == 200
    assert bulk_price(100, 20) == 1800
