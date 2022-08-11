from orator import DatabaseManager, Schema, Model

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": "fastapi_graphql",
        "user": "postgres",
        "password": "myPassword",
        "prefix": "",
        "port": 5432
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
