

from flask_app.config.mysqlconnection import connect_to_mysql

class Ninja:
    """Ninja model class."""

    def __init__(self, data):
        """Constructor."""

        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo = data["dojo_id"]

    @classmethod
    def read_all(cls):
        """Obtener todos los dojos."""
        query = 'SELECT * FROM ninjas;'
        results = connect_to_mysql('dojos_ninjas_schema').query_db(query)
        ninjas =[]

        for n in results:
            ninjas.append(cls(d))
        return ninjas

    @classmethod
    def create(cls, data):
        """Crear un ninja."""
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );'
        return connect_to_mysql('dojo_ninjas').query_db(query, data)
