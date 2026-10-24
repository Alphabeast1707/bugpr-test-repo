import pytest
from inventory import Catalog, Item


def make() -> Catalog:
    c = Catalog()
    c.add(Item("a", "apple", 50, 4))
    c.add(Item("b", "bean", 10, 0))
    return c


def test_add_and_value() -> None:
    c = make()
    assert c.total_value_cents() == 200
    assert [i.sku for i in c.in_stock()] == ["a"]


def test_duplicate_sku_rejected() -> None:
    with pytest.raises(ValueError):
        make().add(Item("a", "apple", 50))


def test_search_exact_case() -> None:
    assert [i.sku for i in make().search("bean")] == ["b"]


def test_remove_returns_item() -> None:
    assert make().remove("a").name == "apple"


def test_remove_missing() -> None:
    with pytest.raises(KeyError):
        make().remove("zzz")
