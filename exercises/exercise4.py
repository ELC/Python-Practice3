"""DataClasses y Sobrecarga de operadores."""

from dataclasses import dataclass
from typing import List




"""Una carrera tiene varias materias, la "longitud" de una carrera hace
referencia a cuantas materias tiene.

Cada materia tiene un nombre.

Escribir una estructura de clases que refleje lo anterior.

Restricciones:
    - Utilizar Dataclasses
    - Utilizar 2 clases
    - Utilizar 1 variables de instancia en cada clase
    - Utilizar 1 método mágico
    - No utilizar variables de clase
    - No utilizar métodos de clase
    - No utilizar métodos de instancia
    - No utilizar properties
    - Utilizar Type Hints en todos los métodos y variables
"""

@dataclass
class Materia(): 
    nombre: str

@dataclass
class Carrera():
    materias: List
    
    #def __str__(self) -> str:
    #    return str([str(i) for i in self.materias])

    def __len__(self) -> int:
        return len(self.materias)




      

matematica = Materia("Matemática")

estadistica = Materia(nombre="Estadística")

obj = Carrera([matematica, estadistica])
print(obj)


# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    materia = Materia()
    assert False, "No se puede instanciar sin nombre"
except TypeError:
    assert True

try:
    materia = Carrera()
    assert False, "No se puede instanciar sin materias"
except TypeError:
    assert True

# Test básico
matematica = Materia("Matemática")
assert matematica.nombre == "Matemática"

estadistica = Materia(nombre="Estadística")
assert estadistica.nombre == "Estadística"

ciclo_basico = Carrera([matematica, estadistica])
assert (
    str(ciclo_basico)
    == "Carrera(materias=[Materia(nombre='Matemática'), Materia(nombre='Estadística')])"  # noqa: 501
)

assert len(ciclo_basico) == 2
# NO MODIFICAR - FIN
