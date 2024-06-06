import sqlite3

def get_items_in_rack(rack_id):
    # Connect to the SQLite database using the absolute path
    db_path = '/home/pi/Python/SMART_VAULT/smartvault.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # SQL query to join the tables and retrieve the specified fields for a specific rack
    query = '''
    SELECT
        item_placement.id AS item_placement_id,
        item_placement.rack_position_id,
        category.name AS category,
        item.item_size,
        item.quantity,
        rack_position.position_label
    FROM
        item_placement
    JOIN
        item ON item_placement.item_id = item.id
    JOIN
        category ON item.category_id = category.id
    JOIN
        rack_position ON item_placement.rack_position_id = rack_position.id
    JOIN
        rack ON rack_position.rack_id = rack.id
    WHERE
        rack.id = ?
    '''
    
    # Execute the query with the specified rack_id
    cursor.execute(query, (rack_id,))
    
    # Fetch all the results
    results = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    return results

# Example usage
rack_id = 1  # Specify the rack_id you want to get the details for
items_in_rack = get_items_in_rack(rack_id)
for item in items_in_rack:
    print(item)