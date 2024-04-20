def saludar():
    print("hola mundo")


class cordialidad():
    def __init__(self,nombre):
        self.nombre=nombre
    def saludar(self):
        print (f"hola soy {self.nombre}")


class cantante():
    def __init__(self,letra):
        self.letra="que bonitos ojitos tienes debajo de esas dos cejas"

    def cantar(self):
        print(f"Coro:{self.letra}")

