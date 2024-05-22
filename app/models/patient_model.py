from database import db

# Define la clase `Libro` que hereda de `db.Model`
# `Libro` representa la tabla `libros` en la base de datos
class Patient(db.Model):
    __tablename__ = "patients"

    # Define las columnas de la tabla `libros`
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    ci = db.Column(db.String(100), nullable=False)
    birth_day = db.Column(db.String(100), nullable=False)

    # Inicializa la clase `Libro`
    def __init__(self, id, name, lastname, ci, birth_day):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.ci = ci
        self.birth_day = birth_day

    # Guarda un libro en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los libros de la base de datos
    @staticmethod
    def get_all():
        return Patient.query.all()

    # Obtiene un libro por su ID
    @staticmethod
    def get_by_id(id):
        return Patient.query.get(id)

    # Actualiza un libro en la base de datos
    def update(self, name=None, lastname=None, ci=None, birth_day=None):
        if name is not None:
            self.name = name
        if lastname is not None:
            self.lastname = lastname
        if ci is not None:
            self.ci = ci
        if birth_day is not None:
            self.birth_day = birth_day
        db.session.commit()

    # Elimina un libro de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()