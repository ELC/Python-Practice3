
import abc
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

# Clase abstracta Contribuyente con método calcular_sueldo()
# Clases concretas: Monotributista Empleado
## variable de instancia ingreso
## redefino calcular_sueldo()

@dataclass
class Contribuyente(ABC):

    @abstractmethod
    def calcular_sueldo() -> float:
        pass

@dataclass
class Monotributista(Contribuyente):
    monto: float

    def calcular_sueldo(self) -> float:
        if(self.monto < (370000/12)):
            return self.monto - 2646.22
        elif(self.monto < (550000/12)):
            return self.monto - 2958.95
        elif(self.monto < (770000/12)):
            return self.monto - 3382.62
        elif(self.monto > (770000/12)):
            return self.monto - 3988.85
        

@dataclass
class Empleado(Contribuyente):
    monto: float

    def calcular_sueldo(self)-> float:
        return self.monto - (self.monto * 0.17)


def calcular_sueldos(contribuyentes: List[Contribuyente]):
    sueldos=[]
    for i in contribuyentes:
        sueldos.append(i.calcular_sueldo())
    return sueldos


# NO MODIFICAR - INICIO
assert type(Contribuyente) == abc.ABCMeta, "Contribuyente debe ser abstracta"
assert issubclass(Empleado, Contribuyente), "Empleado debe heredar de Contribuyente" # noqa: 501
assert issubclass(Monotributista, Contribuyente), "Monotributista debe heredar de Contribuyente" # noqa: 501

try:
    juan = Contribuyente()
    assert False, "No se puede instanciar una clase abstracta"
except TypeError:
    assert True

try:
    juan = Empleado()
    assert False, "No se puede instanciar sin sueldo"
except TypeError:
    assert True

try:
    juan = Monotributista()
    assert False, "No se puede instanciar sin sueldo"
except TypeError:
    assert True


# Test Básico
juan = Monotributista(25_000)
assert juan.calcular_sueldo() == 22353.78

juan = Monotributista(35_000)
assert juan.calcular_sueldo() == 32041.05

juan = Monotributista(50_000)
assert juan.calcular_sueldo() == 46617.38

juan = Monotributista(75_000)
assert juan.calcular_sueldo() == 71011.15


maria = Empleado(25_000)
assert maria.calcular_sueldo() == 20750.0

maria = Empleado(35_000)
assert maria.calcular_sueldo() == 29050.0

maria = Empleado(50_000)
assert maria.calcular_sueldo() == 41500.0

maria = Empleado(75_000)
assert maria.calcular_sueldo() == 62250.0


# Test Calculadora de sueldos

contribuyentes = [Monotributista(80_000), Empleado(80_000)]
# print(calcular_sueldos(contribuyentes))
assert calcular_sueldos(contribuyentes) == [76011.15, 66400.0]

# NO MODIFICAR - FIN