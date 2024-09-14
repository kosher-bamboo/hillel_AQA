import psycopg2
import os
from test_data import create_table_categories, create_table_products, insert_into_categories, insert_into_products

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
