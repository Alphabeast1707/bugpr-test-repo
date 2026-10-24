import pytest
from inventory import paginate


def test_first_page() -> None:
    p = paginate(list(range(20)), 1, page_size=10)
    assert p.items == list(range(10))
    assert p.total_pages == 2
    assert p.has_next


def test_last_page_exact_multiple() -> None:
    p = paginate(list(range(20)), 2, page_size=10)
    assert p.items == list(range(10, 20))
    assert not p.has_next


def test_out_of_range() -> None:
    with pytest.raises(IndexError):
        paginate(list(range(20)), 3, page_size=10)


def test_bad_page_size() -> None:
    with pytest.raises(ValueError):
        paginate([1], 1, page_size=0)
