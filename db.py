from orator import DatabaseManager, Schema, Model

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": "db_name",
        "user": "db_user",
        "password": "db_password",
        "prefix": "",
        "port": 5432
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
