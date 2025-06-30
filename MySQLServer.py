import mysql.connector
print("✅ mysql.connector is working!")

from mysql.connector import Error

try:
    # Connect to MySQL server (no database specified yet)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root'  # 🔁 Replace with your actual password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close connection and cursor safely
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
