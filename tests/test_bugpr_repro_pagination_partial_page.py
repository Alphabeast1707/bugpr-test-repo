from inventory import paginate


def test_partial_last_page_is_included_and_reachable() -> None:
    items = list(range(25))

    second_page = paginate(items, 2, page_size=10)
    assert second_page.items == list(range(10, 20))
    assert second_page.total_pages == 3
    assert second_page.has_next

    third_page = paginate(items, 3, page_size=10)
    assert third_page.items == list(range(20, 25))
    assert third_page.total_pages == 3
    assert not third_page.has_next
