"""El ente regulador de impuestos llama a todas las personas activas
laboralmente Contribuyentes, sin embargo, existen varios tipos de
contribuyentes, por ejemplo, el Monotributista y el que es Empleado en relación
de dependencia. Ambos están dentro del sistema pero pagan diferentes impuestos.

El monotributista tiene que pagar en función de sus ingresos brutos anuales:
    - Si son menores a $370.000, paga $2646,22 mensuales
    - Si son menores a $550.000, paga $2958,95 mensuales
    - Si son menores a $770.000, paga $3382,62 mensuales
    - Si son mayores a $770.000, paga $3988,85 mensuales

En el caso de los empleados en relación de dependencia, ellos pagan un 17% de
impuestos sobre sus ingresos brutos mensuales.

Inspirado en datos reales: https://www.afip.gob.ar/monotributo/categorias.asp

Escribir una estructura de clases que refleje lo anterior. Para simplificar el
análisis, todos los montos serán mensuales (dividir los límites del monotributo
por 12).

Aclaración: Este ejercicio está basado en la realidad pero se realizaron
múltiples simplificaciones para adecuarlo al contexto del curso.

Restricciones:
    - Utilizar Dataclasses
    - Utilizar 3 clases: 1 abstracta y 2 concretas
    - Utilizar 1 variables de instancia en cada clase concreta
    - Utilizar 1 métodos de instancia con polimorfismo
    - No utilizar variables de clase
    - No utilizar métodos de clase
    - No utilizar properties
    - Utilizar Type Hints en todos los métodos y variables
"""

import abc
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


def calcular_sueldos(contribuyentes: List[Contribuyente]):
    """Data una lista de contribuyentes, devuelve una lista de los sueldos de
    cada uno."""


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

assert calcular_sueldos(contribuyentes) == [76011.15, 66400.0]

# NO MODIFICAR - FIN
