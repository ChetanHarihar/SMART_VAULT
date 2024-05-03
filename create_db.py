import sqlite3

# Connect to the SQLite database. If it doesn't exist, it will be created.
conn = sqlite3.connect('smartvault.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Creating the Employee table
# Stores employee details with a unique uid for each employee.
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    uid TEXT NOT NULL UNIQUE,
    role INTEGER NOT NULL
)
''')

# Creating the Categories table
# Represents different categories of items.
cursor.execute('''
CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
''')

# Creating the Items table
# Each item is linked to a category and has a unique size within that category.
# The combination of category_id and item_size is unique.
cursor.execute('''
CREATE TABLE IF NOT EXISTS item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    item_size TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE RESTRICT,
    UNIQUE(category_id, item_size)
)
''')

# Creating the Racks table
# Represents storage racks. Each rack has a unique name.
cursor.execute('''
CREATE TABLE IF NOT EXISTS rack (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
''')

# Creating the RackPositions table
# Each position within a rack has a unique label, ensuring unique positions within the same rack.
cursor.execute('''
CREATE TABLE IF NOT EXISTS rack_position (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rack_id INTEGER,
    position_label TEXT NOT NULL,
    FOREIGN KEY (rack_id) REFERENCES rack(id) ON DELETE RESTRICT,
    UNIQUE(rack_id, position_label)
)
''')

# Creating the ItemPlacement table
# Maps items to specific rack positions. Each position can hold only one item, and each item can be in only one position.
cursor.execute('''
CREATE TABLE IF NOT EXISTS item_placement (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rack_position_id INTEGER,
    item_id INTEGER,
    FOREIGN KEY (rack_position_id) REFERENCES rack_position(id) ON DELETE RESTRICT,
    FOREIGN KEY (item_id) REFERENCES item(id) ON DELETE RESTRICT,
    UNIQUE(rack_position_id, item_id)
)
''')

# Commit the transaction
conn.commit()

# Close the connection when done
conn.close()