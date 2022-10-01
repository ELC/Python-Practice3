class Piloto:
    def init(self,nombre,apellido,edad,estudiosUniversitarios,pais='NA'):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.estudiosUniversitarios=estudiosUniversitarios
        self.pais=pais

    def mostrar(self):
        print(self.nombre)
        print(self.apellido)
        print(self.edad)
        print(self.estudiosUniversitarios)
        print(self.pais)

    def esMayor(self):
        if(self.edad>17):
            return True
        return False

ejemplo_piloto=Piloto("Juan","Perez",75,False)
#ejemplo_piloto.mostrar()
#print(ejemplo_piloto.esMayor())

#TODO PERFECTO!!!!! 
class Cohete:
    def init(self,modelo,piloto,combustibleTotal,consumoPorKm):
        self.modelo=modelo
        self.piloto=piloto
        self.combustibleTotal=combustibleTotal
        self.consumoPorKm=consumoPorKm

    def mostrar(self):
        print(self.modelo)
       # print(self.piloto) #MAL
        self.piloto.mostrar()
        print(self.combustibleTotal)
        print(self.consumoPorKm)

    def calcularFactibilidad(self,distancia):
        if(self.consumoPorKmint(distancia)<self.combustibleTotal):
            return True
        return False

ejemplo_cohete=Cohete("APOLO 1",ejemplo_piloto,16,1)
ejemplo_cohete.mostrar()
print("Es factible?")
print(ejemplo_cohete.calcularFactibilidad("15"))

