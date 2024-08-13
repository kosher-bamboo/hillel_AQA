import psycopg2

db_name = 'postgres'
host = '127.0.0.1'
port = 5432
user_name = 'postgres'
user_password = 'Qwerty123'

# open connection
connection = psycopg2.connect(
    database=db_name,
    user=user_name,
    password=user_password,
    host=host,
    port=port
)
# open cursor
cursor = connection.cursor()

cursor.execute('SELECT * FROM hw20.products')
list_of_products = cursor.fetchall()

cursor.execute('SELECT * FROM hw20.products p JOIN hw20.categories c ON p.category_id = c.category_id;')
list_of_products_w_categories = cursor.fetchall()

# my_list = cursor.fetchone()

print(list_of_products)
print(list_of_products_w_categories)

cursor.close()
connection.close()
