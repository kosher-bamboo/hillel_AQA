import psycopg2
import os
from test_data import create_table_categories, create_table_products, insert_into_categories, insert_into_products
import pytest
import allure


@allure.title("Database Operations")
class TestDatabase:

    @allure.title("Database connection")
    def test_database_connection(self):
        database_url = os.getenv('DATABASE_URL')
        with allure.step("Connect to DB"):
            conn = psycopg2.connect(database_url)

        assert conn is not None

    @allure.title("Table creation")
    def test_table_creation(self):

        database_url = os.getenv('DATABASE_URL')
        with allure.step("Connect to DB"):
            conn = psycopg2.connect(database_url)
        cursor = conn.cursor()
        with allure.step("Create table 'user'"):
            cursor.execute("DROP TABLE IF EXISTS users;")
            cursor.execute("""CREATE TABLE users (user_id int NOT NULL, name VARCHAR NOT NULL);""")
        conn.commit()
        with allure.step("Table existence check"):
            cursor.execute("SELECT * FROM users")
            conn.commit()

            result = cursor.fetchall()
        assert result is not None


    @allure.title("Data manipulation")
    @pytest.mark.parametrize("query, expected", [
        ("INSERT INTO users (user_id, name) VALUES (1, 'John')", "John"),
        ("UPDATE users SET name = 'John2' WHERE user_id = 1", "John2"),
        ("DELETE FROM users WHERE user_id = 1", None)
    ])
    def test_data_manipulation(self, query, expected):
        database_url = os.getenv('DATABASE_URL')
        with allure.step("Connect to DB"):
            conn = psycopg2.connect(database_url)
        cursor = conn.cursor()
        with allure.step("Query execution"):
            cursor.execute(query)
        conn.commit()
        with allure.step("SELECT data from DB"):
            cursor.execute("SELECT * FROM users WHERE user_id=1")
        conn.commit()
        result = cursor.fetchone()
        if expected is None:
            assert result is None
        else:
            assert result[1] == expected

        cursor.close()
        conn.close()


    @allure.title("Data selection")
    @pytest.mark.parametrize("query, expected", [
        ("SELECT * FROM categories", 0),
        ("SELECT * FROM products", 0),
        ("SELECT * FROM products p JOIN categories c ON p.category_id = c.category_id;", 7)
    ])
    def test_data_selection(self, query, expected):
        # connect to db
        database_url = os.getenv('DATABASE_URL')
        with allure.step("Connect to DB"):
            conn = psycopg2.connect(database_url)

        # create tables
        cursor = conn.cursor()
        with allure.step("Create table Categories"):
            cursor.execute(create_table_categories)
        with allure.step("Create table Products"):
            cursor.execute(create_table_products)
        with allure.step("Insert into Categories"):
            cursor.execute(insert_into_categories)
        with allure.step("Insert into Products"):
            cursor.execute(insert_into_products)
        conn.commit()

        try:
            # run queries, assert results
            with allure.step(f"Query: {query}"):
                cursor.execute(query)
            result = cursor.fetchall()
            if expected == 0:
                assert len(result) > expected
            if expected == 7:
                assert len(result[0]) == expected
        finally:
            # Drop tables after the assertion
            with allure.step("Drop DB Products"):
                cursor.execute("DROP TABLE IF EXISTS products;")
            with allure.step("Drop DB Categories"):
                cursor.execute("DROP TABLE IF EXISTS categories;")
            conn.commit()

            # Clean up resources
            with allure.step("Close connection"):
                cursor.close()
                conn.close()
