import mysql.connector
import os
from dotenv import load_dotenv


class DBManager:
    def __init__(self) -> None:
        """
        Initializes the DBManager class by establishing a connection to the database using environment variables.
        """
        load_dotenv()
        host: str = os.getenv('DB_HOST', 'localhost')
        user: str = os.getenv('DB_USER', 'root')
        password: str = os.getenv('DB_PASSWORD', 'rootDSV')
        database: str = os.getenv('DB_DATABASE', 'sakila')

        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            raise

    def execute_query(self, query: str, params: tuple = None) -> list[dict]:
        """
        Executes a given SQL query with optional parameters.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters to substitute into the query.

        Returns:
            list[dict]: The result of the query as a list of dictionaries (for SELECT queries).
        """
        try:
            self.cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return []
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return []

    def close(self) -> None:
        """
        Closes the database connection and cursor.

        Returns:
            None
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except mysql.connector.Error as err:
            print(f"Error closing database connection: {err}")
