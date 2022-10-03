import abc
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class Contribuyente(ABC): 

    sueldo: float
    contribuyentes: List=None

    def calcular_sueldos(contribuyentes: List=[]):
        return contribuyentes.calcular_sueldo()

   # """Dada una lista de contribuyentes, devuelve una lista de los sueldos de
   # cada uno."""
@dataclass
class Monotributista(Contribuyente):

    def calcular_sueldo(self) -> float:
        if self.sueldo < 30833:
           return self.sueldo - 2646.22
        elif self.sueldo < 45833:
            return self.sueldo - 2958.95
        elif self.sueldo < 64166:
            return self.sueldo - 3382.62
        elif self.sueldo > 64166:
            return self.sueldo - 3988.85

@dataclass
class Empleado(Contribuyente):

    def calcular_sueldo(self) -> float:  
        return self.sueldo - self.sueldo * 0.17  

   
juan = Monotributista(80000)
maria = Empleado(80_000)
print(maria.calcular_sueldo())
print(juan.calcular_sueldo())