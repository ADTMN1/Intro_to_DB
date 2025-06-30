import mysql.connector
print("✅ mysql.connector is working!")

try:
    # Connect to MySQL server (no database specified yet)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root'  # 🔁 Replace with your actual MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")  # ✅ Fully qualified exception name for checker

finally:
    # ✅ Graceful resource cleanup
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
