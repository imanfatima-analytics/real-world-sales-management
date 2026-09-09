def calculate_sales(quantity, unit_price, discount_pct):
    return quantity * unit_price * (1 - discount_pct / 100)


def test_sales_without_discount():
    result = calculate_sales(2, 1000, 0)
    assert result == 2000


def test_sales_with_discount():
    result = calculate_sales(1, 1000, 10)
    assert result == 900


def test_sales_with_five_percent_discount():
    result = calculate_sales(1, 185000, 5)
    assert result == 175750