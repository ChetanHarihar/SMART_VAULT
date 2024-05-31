# item placement

import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('smartvault.db')
cursor = conn.cursor()

# Prepare a list of item placements to insert
placements = [(11, 20),(12, 21),(13, 22),(14, 23),(15, 24),(16, 25),(17, 26),(18, 27),(19, 28),(20, 29),(21, 30),(22, 31),(23, 39),(24, 40),(25, 41),(26, 42),(27, 43),(28, 44)]  # Each tuple is (rack_position_id, item_id)

# Insert multiple item placements
cursor.executemany("INSERT INTO item_placement (rack_position_id, item_id) VALUES (?, ?)", placements)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()