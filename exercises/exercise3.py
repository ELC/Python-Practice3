class Article:
    
    iva = 0.21    

    def init(self, nombre, costo, descuento = 0.00):
        self.nombre: str = nombre
        self.costo: float = costo
        self.descuento: float = descuento
        
        
    @property
    def precio(self) -> float:
        subtotal = self.costo - self.costo * self.descuento
        total_con_iva = subtotal * (1 + self.iva)
        return round(total_con_iva, 2)    
    
    @classmethod
    def actualizar_iva(cls, iva):
        cls.iva = iva





    



# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    article = Article()
    assert False, "No se puede instanciar sin nombre ni costo"
except TypeError:
    assert True

try:
    article = Article("Auto")
    assert False, "No se puede instanciar sin costo"
except TypeError:
    assert True

try:
    article = Article(nombre="Auto", costo=1)
    assert True
except TypeError:
    assert False, "El descuento es opcional"

try:
    article = Article(nombre="Auto", costo=1)
    article.precio = 2
    assert False, "No se puede modificar el precio"
except AttributeError:
    assert True


# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.precio == 1.21


article = Article("Auto", 1, 0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.25
# NO MODIFICAR - FIN
