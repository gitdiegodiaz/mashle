def saludar():
    print("hola mundo")


class presentacion():
    def __init__(self,nombre):
        self.nombre=nombre
    def saludar(self):
        print (f"hola soy {self.nombre}")
