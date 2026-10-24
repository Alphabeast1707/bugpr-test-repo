from __future__ import annotations

BULK_THRESHOLD = 10
BULK_DISCOUNT_PERCENT = 10


def apply_discount(price_cents: int, percent: int) -> int:
    """Price after a percentage discount, rounded half up to the nearest cent."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return (price_cents * (100 - percent) + 50) // 100


def bulk_price(unit_cents: int, quantity: int) -> int:
    """Total for `quantity` units; orders of BULK_THRESHOLD or more get the bulk discount."""
    total = unit_cents * quantity
    if quantity >= BULK_THRESHOLD:
        return apply_discount(total, BULK_DISCOUNT_PERCENT)
    return total
