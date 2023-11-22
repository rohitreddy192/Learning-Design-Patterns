"""

The Factory Design Pattern is a creational pattern used to create objects without specifying the exact class of object that 
will be created. It provides a way to create objects based on a common interface, allowing the creation of objects without 
exposing the instantiation logic to the client.

Use Case: Database Connection

Suppose you are working on an application that needs to communicate with various types of databases like Oracle, MySQL, or PostgreSQL. 
The Factory Pattern can be used to create a connection to these databases. You can have a DatabaseFactory that has a method 
createConnection. The specific database connection classes (OracleConnection, MySQLConnection, PostgreSQLConnection) would be created by 
this factory method, allowing the client code to remain unaware of the concrete database connection type. 
The connection type could be specified in configuration or dynamically at runtime.

"""


# Interface for database connection
class DatabaseConnection:
    def connect(self):
        pass

# Concrete database connection classes
class OracleConnection(DatabaseConnection):
    def connect(self):
        print("Connected to Oracle database")

class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Connected to MySQL database")

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("Connected to PostgreSQL database")

# Database connection factory
class DatabaseConnectionFactory:
    @staticmethod
    def create_connection(db_type):
        if db_type == "Oracle":
            return OracleConnection()
        elif db_type == "MySQL":
            return MySQLConnection()
        elif db_type == "PostgreSQL":
            return PostgreSQLConnection()
        else:
            raise ValueError("Invalid database type")

if __name__ == "__main__":
    # Usage example
    factory = DatabaseConnectionFactory()

    # Create a connection based on configuration or runtime input
    db_type = "MySQL"  # This type could come from configuration or user input
    connection = factory.create_connection(db_type)
    connection.connect()

"""
Interface (DatabaseConnection): Defines the common method connect that all concrete database connection classes should implement.
Concrete Classes (OracleConnection, MySQLConnection, PostgreSQLConnection): Implement the interface and define specific behavior for connecting to their respective databases.
Factory (DatabaseConnectionFactory): Provides a method (create_connection) to create instances of different database connection types based on the provided input.

"""