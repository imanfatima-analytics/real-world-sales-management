import pandas as pd
from sqlalchemy import create_engine


# ============================================================
# 1. DATABASE CONNECTION
# ============================================================

engine = create_engine(
    "postgresql+psycopg2://postgres:pakistan1@localhost:5432/real_world_sales"
)


# ============================================================
# 2. LOAD DATA FROM POSTGRESQL
# ============================================================

customers = pd.read_sql(
    "SELECT * FROM customers;",
    engine
)

orders = pd.read_sql(
    "SELECT * FROM orders;",
    engine
)

order_items = pd.read_sql(
    "SELECT * FROM order_items;",
    engine
)

products = pd.read_sql(
    "SELECT * FROM products;",
    engine
)


# ============================================================
# 3. CALCULATE SALES AMOUNT
# ============================================================

order_items["sales_amount"] = (
    order_items["quantity"]
    * order_items["unit_price"]
    * (1 - order_items["discount_pct"] / 100)
)


# ============================================================
# 4. ORDER-LEVEL SALES
# ============================================================

order_totals = (
    order_items
    .groupby("order_id")["sales_amount"]
    .sum()
)


# ============================================================
# 5. BUSINESS KPIs
# ============================================================

total_sales = order_totals.sum()

total_orders = order_totals.count()

average_order_value = order_totals.mean()

total_quantity_sold = order_items["quantity"].sum()

total_customers = customers["customer_id"].nunique()


print("\n===================================")
print("          BUSINESS KPIs")
print("===================================")

print("Total Sales:", round(total_sales, 2))
print("Total Orders:", total_orders)
print("Average Order Value:", round(average_order_value, 2))
print("Total Quantity Sold:", total_quantity_sold)
print("Total Customers:", total_customers)


# ============================================================
# 6. CUSTOMER ANALYSIS
# ============================================================

sales = order_items.merge(
    orders[["order_id", "customer_id", "order_date"]],
    on="order_id"
)

sales = sales.merge(
    customers[["customer_id", "customer_name", "city"]],
    on="customer_id"
)


customer_sales = (
    sales
    .groupby(
        ["customer_id", "customer_name", "city"]
    )["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)


print("\n===================================")
print("        TOP 5 CUSTOMERS")
print("===================================")

print(customer_sales.head(5))


# ============================================================
# 7. PRODUCT ANALYSIS
# ============================================================

product_sales = order_items.merge(
    products[
        ["product_id", "product_name", "category"]
    ],
    on="product_id"
)


product_analysis = (
    product_sales
    .groupby(
        ["product_id", "product_name", "category"]
    )
    .agg(
        total_quantity=("quantity", "sum"),
        total_sales=("sales_amount", "sum")
    )
    .sort_values(
        "total_sales",
        ascending=False
    )
)


print("\n===================================")
print("        TOP 5 PRODUCTS")
print("===================================")

print(product_analysis.head(5))


# ============================================================
# 8. CATEGORY ANALYSIS
# ============================================================

category_analysis = (
    product_sales
    .groupby("category")
    .agg(
        total_quantity=("quantity", "sum"),
        total_sales=("sales_amount", "sum")
    )
    .sort_values(
        "total_sales",
        ascending=False
    )
)


print("\n===================================")
print("        CATEGORY PERFORMANCE")
print("===================================")

print(category_analysis)


# ============================================================
# 9. MONTHLY SALES TREND
# ============================================================

sales["order_date"] = pd.to_datetime(
    sales["order_date"]
)

sales["month"] = sales["order_date"].dt.to_period("M")


monthly_sales = (
    sales
    .groupby("month")["sales_amount"]
    .sum()
    .sort_index()
)


print("\n===================================")
print("        MONTHLY SALES")
print("===================================")

print(monthly_sales)


# ============================================================
# 10. TOP PRODUCT
# ============================================================

top_product_name = product_analysis.index[0][1]

top_product_sales = product_analysis.iloc[0]["total_sales"]


print("\n===================================")
print("          TOP PRODUCT")
print("===================================")

print(
    "Product:",
    top_product_name
)

print(
    "Sales:",
    round(top_product_sales, 2)
)


# ============================================================
# 11. TOP CATEGORY
# ============================================================

top_category_name = category_analysis.index[0]

top_category_sales = category_analysis.iloc[0]["total_sales"]


print("\n===================================")
print("          TOP CATEGORY")
print("===================================")

print(
    "Category:",
    top_category_name
)

print(
    "Sales:",
    round(top_category_sales, 2)
)


# ============================================================
# 12. TOP CUSTOMER
# ============================================================

top_customer_name = customer_sales.index[0][1]

top_customer_sales = customer_sales.iloc[0]


print("\n===================================")
print("          TOP CUSTOMER")
print("===================================")

print(
    "Customer:",
    top_customer_name
)

print(
    "Sales:",
    round(top_customer_sales, 2)
)


# ============================================================
# 13. FINAL BUSINESS SUMMARY
# ============================================================

print("\n===================================")
print("       FINAL BUSINESS SUMMARY")
print("===================================")

print(
    "Total Sales:",
    round(total_sales, 2)
)

print(
    "Total Orders:",
    total_orders
)

print(
    "Average Order Value:",
    round(average_order_value, 2)
)

print(
    "Total Quantity Sold:",
    total_quantity_sold
)

print(
    "Total Customers:",
    total_customers
)

print(
    "Top Customer:",
    top_customer_name
)

print(
    "Top Product:",
    top_product_name
)

print(
    "Top Category:",
    top_category_name
)


# ============================================================
# 14. COMPLETION MESSAGE
# ============================================================

print("\n===================================")
print("   PYTHON ANALYSIS COMPLETED")
print("===================================")