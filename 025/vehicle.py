from datetime import date
class vehicle():
    def __init__(self, id: int, modelo:str,marca:str,matricula:str,fechaMatriculacion:date,nombrePropietario:str):
        self._id = id
        self._modelo = modelo
        self._marca = marca
        self._matricula = matricula
        self._fechaMatriculacion = fechaMatriculacion
        self._nombrePropietario = nombrePropietario

    def partes(self):
        print("ID: ",self._id)
        print("Modelo: ",self._modelo)
        print("Marca: ",self._marca)
        print("Matricula: ",self._matricula)
        print("Fecha de matriculacion: ",self._fechaMatriculacion)
        print("Nombre del propietario: ",self._nombrePropietario)
    def toDict(self):
        return {
        "id": self._id,
        "modelo": self._modelo,
        "marca": self._marca,
        "matricula": self._matricula,
        "fechaMatriculacion": self._fechaMatriculacion,
        "nombrePropietario": self._nombrePropietario
    }
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,value):
        self._id = value
    
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self,valor):
        self._modelo = valor
    
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,valor):
        self._marca = valor
    
    @property
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self,valor):
        self._matricula = valor

    @property
    def fechaMatriculacion(self):
        return self._fechaMatriculacion
    @fechaMatriculacion.setter
    def fechaMatriculacion(self,valor):
        self._fechaMatriculacion = valor

    @property
    def nombrePropietario(self):
        return self._nombrePropietario
    @nombrePropietario.setter
    def nombrePropietario(self,valor):
        self._nombrePropietario = valor
        
vehiculo = vehicle(
    id=1,
    modelo="Modelo s",
    marca="Tesla",
    matricula="1234",
    fechaMatriculacion=date(2020,5,20),
    nombrePropietario="Angel andres"
)

vehiculo.partes()
vehiculo_dict = vehiculo.toDict()

print(vehiculo_dict)
