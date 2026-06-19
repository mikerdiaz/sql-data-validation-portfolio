import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    country TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

customers = [
    (1, "Maria Gonzalez", "maria@example.com", "Chile"),
    (2, "John Smith", "john@example.com", "Canada"),
    (3, "Ana Torres", "ana@example.com", "Venezuela"),
]

orders = [
    (1, 1, "2026-01-15", 150.00),
    (2, 2, "2026-02-10", 89.50),
    (3, 1, "2026-03-05", 220.75),
    (4, 99, "2026-03-08", 50.00),
]

cursor.executemany("INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?)", customers)
cursor.executemany("INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?)", orders)

conn.commit()
conn.close()
print("Database created successfully.")