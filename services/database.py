import sqlite3

def fetch_categories():
    conn = sqlite3.connect('/home/pi/Python/SMART_VAULT/smartvault.db')
    cursor = conn.cursor()

    cursor.execute('''
                   SELECT name FROM category
    ''')
    
    categories = cursor.fetchall()
    conn.close()
    # Extract category names from the list of tuples
    category_names = [category[0] for category in categories]
    return category_names

def fetch_all_items(categories):
    conn = sqlite3.connect('/home/pi/Python/SMART_VAULT/smartvault.db')
    cursor = conn.cursor()

    all_items = {}

    for category in categories:
        cursor.execute('''
                        SELECT Item.id AS ItemID, category.name AS CategoryName, item.item_size AS ItemSize, item.quantity AS Quantity
                        FROM item
                        INNER JOIN category ON item.category_id = category.id
                        WHERE category.name = ?
            ''', (category,))
        
        items = cursor.fetchall()
        all_items[category] = items

    conn.close()
    return all_items

def get_rack_and_position(item_ids):
    # Initialize an empty dictionary to hold the results
    results_dict = {}
    
    # Connect to the SQLite database
    conn = sqlite3.connect("/home/pi/Python/SMART_VAULT/smartvault.db")
    cursor = conn.cursor()
    
    
    # SQL query to fetch item ID, rack name, and position label for specified item IDs
    query = f"""
    SELECT
        ip.item_id,
        r.name AS RackName,
        rp.position_label AS PositionLabel
    FROM
        item_placement ip
    INNER JOIN
        rack_position rp ON ip.rack_position_id = rp.id
    INNER JOIN
        rack r ON rp.rack_id = r.id
    WHERE
        ip.item_id IN ({','.join('?'*len(item_ids))});
    """
    
    try:
        # Execute the query with the item_ids_tuple
        cursor.execute(query, item_ids)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Populate the results dictionary
        for item_id, rack_name, position_label in results:
            results_dict[item_id] = (rack_name, position_label)
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()
    
    # Sort the dictionary by the rack part first, then the label part
    # and return the sorted dictionary
    return {k: v for k, v in sorted(results_dict.items(), key=lambda item: (item[1][0], item[1][1]))}

def update_item_quantity(item_id, subtract_amount):
    conn = sqlite3.connect('/home/pi/Python/SMART_VAULT/smartvault.db')
    cursor = conn.cursor()
    
    try:
        # Fetch the current quantity of the item
        cursor.execute('SELECT quantity FROM item WHERE id = ?', (item_id,))
        result = cursor.fetchone()
        
        current_quantity, = result
        
        new_quantity = current_quantity - subtract_amount
        
        # Update the item with the new quantity
        cursor.execute('UPDATE item SET quantity = ? WHERE id = ?', (new_quantity, item_id))
        conn.commit()
    
    except sqlite3.Error as e:
        print("An error occurred:", e)
        conn.rollback()  # Rollback any changes if something goes wrong
    
    finally:
        # Always close the connection to the database
        conn.close()