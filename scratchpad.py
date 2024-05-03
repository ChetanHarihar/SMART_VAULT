import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('smartvault.db')
cursor = conn.cursor()

# Prepare a list of item placements to insert
placements = [(6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]  # Each tuple is (rack_position_id, item_id)

# Insert multiple item placements
cursor.executemany("INSERT INTO item_placement (rack_position_id, item_id) VALUES (?, ?)", placements)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()