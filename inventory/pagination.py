from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Page(Generic[T]):
    number: int
    items: list[T]
    total_pages: int

    @property
    def has_next(self) -> bool:
        return self.number < self.total_pages


def page_count(n_items: int, page_size: int) -> int:
    if page_size <= 0:
        raise ValueError("page_size must be positive")
    return n_items // page_size


def paginate(items: list[T], page: int, page_size: int = 10) -> Page[T]:
    """Return the 1-indexed `page` of `items`."""
    total = page_count(len(items), page_size)
    if page < 1 or (total and page > total):
        raise IndexError(f"page {page} out of range (1..{total})")
    start = (page - 1) * page_size
    return Page(number=page, items=items[start : start + page_size], total_pages=total)
