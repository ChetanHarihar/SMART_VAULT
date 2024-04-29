def check_scan_result(q):
    try:
        result = q.get_nowait()
        if result[0] == 'Success':
            uid, text, role = result[1], result[2].strip(), result[3]
            conn = sqlite3.connect('/home/pi/Python/SMART_VAULT/smartvault.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, role FROM employee WHERE uid = ?", (uid,))
            fetched_result = cursor.fetchone()
            conn.close()

            if fetched_result is not None and fetched_result[-1] == role:
                name_label.config(text=f"Logged in as: {text}")
                forget_frame(scan_frame, success_frame)
            else:
                failed_label.config(text="Access Denied. Trying again...")
                forget_frame(scan_frame, failed_frame)
                root.after(3500, restart_scan)
        else:
            failed_label.config(text="Scan Failed. Trying again...")
            forget_frame(scan_frame, failed_frame)
            root.after(3500, restart_scan)
    except queue.Empty:
        root.after(500, lambda: check_scan_result(q))
