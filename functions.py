import sqlite3

# 1. Create connection to db 
def create_table():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    print('Tablet created')
    return cursor

# 2. add rows to db
def index():
    conn = create_table()
    products = conn.execute("""CREATE TABLE inventory(
                            product_name TEXT,
                            product_quantity INTEGER,
                            product_price REAL
                            )""")
    print('Created inventory')
    conn.close()
    return products


new_inv = index()
