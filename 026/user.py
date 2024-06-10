class User:
    def __init__(self, id: int, nombre: str, segundoNombre: str, apellidos: str, edad: int, email: str):
        self._id = id
        self._nombre = nombre
        self._segundoNombre = segundoNombre
        self._apellidos = apellidos
        self._edad = edad
        self._email = email
    
    def partes(self):
        print("id: ", self._id)
        print("nombre: ", self._nombre)
        print("segundoNombre: ", self._segundoNombre)
        print("apellidos: ", self._apellidos)
        print("edad: ", self._edad)
        print("email: ", self._email)
    
    def toDict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "segundoNombre": self._segundoNombre,
            "apellidos": self._apellidos,
            "edad": self._edad,
            "email": self._email
        }
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def segundoNombre(self):
        return self._segundoNombre

    @segundoNombre.setter
    def segundoNombre(self, valor):
        self._segundoNombre = valor

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, valor):
        self._apellidos = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

user = User(
    id=1,
    nombre="Juan",
    segundoNombre="Carlos",
    apellidos="Pérez López",
    edad=30,
    email="juan.perez@example.com"
)

user.partes()

user_dict = user.toDict()
print(user_dict)
