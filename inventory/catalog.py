from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Item:
    sku: str
    name: str
    price_cents: int
    quantity: int = 0


@dataclass
class Catalog:
    items: dict[str, Item] = field(default_factory=dict)

    def add(self, item: Item) -> None:
        if item.sku in self.items:
            raise ValueError(f"duplicate sku: {item.sku}")
        self.items[item.sku] = item

    def remove(self, sku: str) -> Item:
        if sku not in self.items:
            raise KeyError(sku)
        item = self.items[sku]
        del self.items[sku]
        return item

    def search(self, query: str) -> list[Item]:
        """Items whose name contains `query`, case-insensitively, sorted by sku."""
        q = query.lower()
        return sorted((i for i in self.items.values() if q in i.name.lower()), key=lambda i: i.sku)

    def in_stock(self) -> list[Item]:
        return sorted((i for i in self.items.values() if i.quantity > 0), key=lambda i: i.sku)

    def total_value_cents(self) -> int:
        return sum(i.price_cents * i.quantity for i in self.items.values())
