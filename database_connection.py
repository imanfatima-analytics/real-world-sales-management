import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="real_world_sales",
    user="postgres",
    password="pakistan1",
    port="5432"
)

cursor = connection.cursor()

cursor.execute("""
    SELECT
        p.product_name,
        SUM(oi.quantity) AS total_quantity_sold
    FROM products AS p
    JOIN order_items AS oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_name
    ORDER BY total_quantity_sold DESC;
""")

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
connection.close()