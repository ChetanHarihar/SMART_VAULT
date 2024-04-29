# rfid_module.py
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sqlite3

# Setup GPIO warnings
GPIO.setwarnings(False)

def scan_rfid(q):
    """
    Clears the queue and then scans an RFID tag using the RFID reader, 
    putting the result into the queue.

    Args:
    q (queue.Queue): The queue to put the scan result.
    """
    try:
        while not q.empty():
            q.get_nowait()  # Clear the queue
    except queue.Empty:
        pass
    
    reader = SimpleMFRC522()
    try:
        uid, text = reader.read()
        print(f"UID: {uid}")
        print(f"TEXT: {text}")
        q.put(('Success', uid, text))
    except Exception as e:
        q.put(('Failed',))
    finally:
        GPIO.cleanup()

def check_scan_result(q, role):
    """
    Checks the RFID scan result and returns True or False accordingly.

    Args:
    q (queue.Queue): The queue from which to get the scan result.
    role (str): The role expected from the RFID scan.

    Returns:
    bool: True if the scan result is successful and matches the role, False otherwise.
    """
    try:
        result = q.get_nowait()
        if result[0] == 'Success':
            uid = result[1]
            conn = sqlite3.connect('/home/pi/Python/SMART_VAULT/employee_info.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, role FROM employee WHERE uid = ?", (uid,))
            fetched_result = cursor.fetchone()
            conn.close()

            if fetched_result is not None and fetched_result[-1] == role:
                print("Access Granted")
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            return False
    except queue.Empty:
        return False


if __name__ == "__main__":
    import queue
    import time
    
    test_queue = queue.Queue()

    scan_rfid(q=test_queue)

    check_scan_result(q=test_queue, role=1)