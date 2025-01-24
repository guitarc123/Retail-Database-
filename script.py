import sqlite3

# Establish connection to the SQLite database
connection = sqlite3.connect("store.db")
cursor = connection.cursor()

# Drop the `purchases` table if it exists
cursor.execute("DROP TABLE IF EXISTS purchases")

# Drop the `stores` table if it exists
cursor.execute("DROP TABLE IF EXISTS stores")

# Create the `stores` table
command1 = """
CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY, 
    location TEXT
)
"""
cursor.execute(command1)

# Create the `purchases` table
command2 = """
CREATE TABLE purchases (
    purchase_id INTEGER PRIMARY KEY, 
    store_id INTEGER, 
    total_cost FLOAT,
    FOREIGN KEY(store_id) REFERENCES stores(store_id)
)
"""
cursor.execute(command2)

# Insert data into the `stores` table
cursor.execute("INSERT INTO stores (store_id, location) VALUES (21, 'London, MN')")
cursor.execute("INSERT INTO stores (store_id, location) VALUES (22, 'London, BN')")
cursor.execute("INSERT INTO stores (store_id, location) VALUES (23, 'Surrey, ON')")

# Insert data into the `purchases` table
cursor.execute("INSERT INTO purchases (purchase_id, store_id, total_cost) VALUES (1, 21, 23.45)")
cursor.execute("INSERT INTO purchases (purchase_id, store_id, total_cost) VALUES (2, 22, 25.47)")

# Retrieve and print all data from the `purchases` table
cursor.execute("SELECT * FROM purchases")
results = cursor.fetchall()
print(results)

# Commit changes and close the connection
connection.commit()
connection.close()

