from flask_app.config.mysqlconnection import connect_to_mysql
from .ninja import Ninja


class Dojo:
    """Dojo model class."""

    def __init__(self, data):
        """Constructor."""

        self.id = data["id"]
        self.name = data["name"]
        self.ninjas =[]


    @classmethod
    def read_all(cls):
        """Obtener todos los dojos."""
        query = 'SELECT * FROM dojos;'
        results = connect_to_mysql('dojos_ninjas_schema').query_db(query)
        dojos =[]

        for d in results:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def create(cls, data):
        """Crear un dojo."""
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        result = connect_to_mysql('dojos_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_one_with_ninjas(cls,data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connect_to_mysql('dojo_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                first_name: row['first_name'],
                last_name: row['last_name'],
                age: row['age']
            }
            dojo.ninjas.append(Ninja(n))
        return dojo
