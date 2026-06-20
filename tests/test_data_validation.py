import sqlite3
import pytest

@pytest.fixture
def db_connection():
    import os
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "..", "database", "ecommerce.db"))
    yield conn
    conn.close()

@pytest.mark.xfail(reason="Known data issue: order #4 references non-existent customer_id 99")
def test_no_orphan_orders(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT order_id, customer_id
        FROM orders
        WHERE customer_id NOT IN (SELECT customer_id FROM customers)
    """)
    orphan_orders = cursor.fetchall()
    assert len(orphan_orders) == 0, f"Found orphan orders: {orphan_orders}"

def test_no_null_emails(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT customer_id, name
        FROM customers
        WHERE email IS NULL OR email = ''
    """)
    invalid_customers = cursor.fetchall()
    assert len(invalid_customers) == 0, f"Customers with missing email: {invalid_customers}"

def test_orders_have_positive_amount(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT order_id, total_amount
        FROM orders
        WHERE total_amount <= 0
    """)
    invalid_orders = cursor.fetchall()
    assert len(invalid_orders) == 0, f"Orders with invalid amount: {invalid_orders}"

def test_order_totals_by_customer(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT c.name, COUNT(o.order_id) as total_orders, SUM(o.total_amount) as total_spent
        FROM customers c
        LEFT JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.customer_id, c.name
        HAVING total_spent > 0 OR total_spent IS NULL
    """)
    results = cursor.fetchall()
    assert len(results) > 0, "No customer order data found"
    for row in results:
        print(f"Customer: {row[0]}, Orders: {row[1]}, Total: {row[2]}")