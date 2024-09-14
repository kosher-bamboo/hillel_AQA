import psycopg2
import os
# from test_data import create_table_categories, create_table_products, insert_into_categories, insert_into_products

import pytest


def test_database_connection():
    database_url = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(database_url)

    assert conn is not None


def test_table_creation():
    database_url = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute("""CREATE TABLE users (user_id int NOT NULL, name VARCHAR NOT NULL);""")
    cursor.execute("SELECT * FROM users")

    result = cursor.fetchall()
    assert result is not None


@pytest.mark.parametrize("query, expected", [
    ("INSERT INTO users (user_id, name) VALUES (1, 'John')", "John"),
    ("UPDATE users SET name = 'John2' WHERE user_id = 1", "John2"),
    ("DELETE FROM users WHERE user_id = 1", None)
])
def test_data_manipulation(query, expected):
    database_url = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.execute("SELECT * FROM users WHERE user_id=1")
    conn.commit()
    result = cursor.fetchone()
    if expected is None:
        assert result is None
    else:
        assert result[1] == expected

    cursor.close()
    conn.close()


@pytest.mark.parametrize("query, expected", [
    ("SELECT * FROM categories", 0),
    ("SELECT * FROM products", 0),
    ("SELECT * FROM products p JOIN categories c ON p.category_id = c.category_id;", 7)
])
def test_data_selection(query, expected):
    create_table_categories = """CREATE TABLE categories (
        category_id int NOT NULL,
        title varchar NOT NULL,
        CONSTRAINT categories_pk PRIMARY KEY (category_id)
        );"""

    create_table_products = """CREATE TABLE products (
        product_id int NOT NULL,
        title varchar NOT NULL,
        description varchar NULL,
        price int NULL,
        category_id int NOT NULL,
        CONSTRAINT products_pk PRIMARY KEY (product_id),
        CONSTRAINT products_categories_fk FOREIGN KEY (category_id) REFERENCES categories(category_id)
        );"""

    insert_into_categories = """INSERT INTO categories
        (category_id, title)
        values
        (1, 'Electronics'),
        (2, 'Personal Care'),
        (3, 'Food and Beverage'),
        (4, 'Home and Kitchen'),
        (5, 'Another category');"""

    insert_into_products = """INSERT INTO products
        (product_id, title, description, price, category_id)
        values
        (1, 'SmartTrack Fitness Watch', 'Advanced fitness tracker with heart rate monitoring and GPS', 129.99, 1),
        (2, 'EcoClean Bamboo Toothbrush Set', 'Biodegradable toothbrushes made from sustainable bamboo', 14.99, 2),
        (3, 'Gourmet Coffee Bean Sampler', 'Assortment of premium coffee beans from around the world', 34.99, 3),
        (4, 'Wireless Noise-Canceling Headphones', 'High-quality over-ear headphones with active noise cancellation', 249.99, 1),
        (5, 'Organic Lavender Essential Oil', '100% pure essential oil for aromatherapy and relaxation', 19.99, 2),
        (6, 'Portable Solar Charger', 'Compact solar panel for charging devices on the go', 59.99, 1),
        (7, 'Reusable Silicone Food Storage Bags', 'Eco-friendly alternative to disposable plastic bags', 24.99, 4),
        (8, 'Ceramic Nonstick Cookware Set', '10-piece set of durable, non-toxic cookware', 159.99, 4),
        (9, 'Smart LED Light Bulb Pack', 'Wi-Fi enabled color-changing bulbs compatible with voice assistants', 39.99, 1),
        (10, 'Ergonomic Memory Foam Pillow', 'Contoured pillow for optimal neck and spine alignment', 49.99, 2);"""

    # connect to db
    database_url = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(database_url)

    # create tables
    cursor = conn.cursor()
    cursor.execute(create_table_categories)
    cursor.execute(create_table_products)
    cursor.execute(insert_into_categories)
    cursor.execute(insert_into_products)
    conn.commit()

    try:
        # run queries, assert results
        cursor.execute(query)
        result = cursor.fetchall()
        if expected == 0:
            assert len(result) > expected
        if expected == 7:
            assert len(result[0]) == expected
    finally:
        # Drop tables after the assertion
        cursor.execute("DROP TABLE IF EXISTS products;")
        cursor.execute("DROP TABLE IF EXISTS categories;")
        conn.commit()

        # Clean up resources
        cursor.close()
        conn.close()
