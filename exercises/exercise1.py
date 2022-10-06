class Circle:
    def _init_(self, radio:float) -> None:
        self.radio: float  = radio

    def area(self) -> float:
        resultado = 3.14 * self.radio **2
        return resultado

    def perimetro(self) -> float:
        resultado = 2 * 3.14 * self.radio
        return resultado       
            
            
            

# NO MODIFICAR - INICIO
# Test básico
circle = Circle()
assert circle.radio == 1
assert circle.area() == 3.14
assert circle.perimetro() == 6.28

# Test palabra clave
circle = Circle()
assert circle.radio == 1
assert circle.area() == 3.14
assert circle.perimetro() == 6.28

# Test parámetro obligatorio
try:
    circle = Circle()
    assert False, "No se puede instanciar sin radio"
except TypeError:
    assert True

# Test invocación encadenada
assert Circle().area() == 3.14
assert Circle().perimetro() == 6.28
# NO MODIFICAR - FIN
