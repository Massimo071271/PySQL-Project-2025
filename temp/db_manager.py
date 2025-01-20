import mysql.connector
import os
from dotenv import load_dotenv


class DBManager:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        host = os.getenv('DB_HOST', 'localhost')
        user = os.getenv('DB_USER', 'root')
        password = os.getenv('DB_PASSWORD', 'rootDSV')
        database = os.getenv('DB_DATABASE', 'sakila')

        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()
            else:
                self.connection.commit()  # Commit для INSERT/UPDATE/DELETE
                return []
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return []

    def close(self):
        self.cursor.close()
        self.connection.close()
