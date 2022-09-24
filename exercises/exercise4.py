from dataclasses import dataclass
from pickle import LONG_BINPUT
from dataclasses import dataclass
import dataclasses
from typing import List

@dataclass
class Materia:
    nombre: str  
    
@dataclass
class Carrera:
    materias: List[Materia]
   
def _len_(self):
    return len(self.materias)          
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