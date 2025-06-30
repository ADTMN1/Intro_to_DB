import mysql.connector
from mysql.connector import Error

print("✅ mysql.connector is working!")

try:
    # Connect to MySQL server (no database specified yet)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")  # ✅ Exception is handled and printed clearly

finally:
    # ✅ Graceful resource cleanup
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
