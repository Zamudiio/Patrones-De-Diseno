#### Estructura de factory method ####

from abc import ABC, abstractmethod

#### CLASE CREADORA ####


class Creator(ABC):
    @abstractmethod
    def create_product():
        return IProduct()

    def some_operation(self):
        p = self.create_product()
        result = f"creador:\n\tEl código del creador a funcionado con: {p.show_data()}"
        return result

#### CLASES CREADORAS CONCRETAS ####


class ConcreteCreatorA(Creator):
    def create_product(self):
        return ConcreteProductA()

    # def some_operation(self):
    #     producto_a = self.create_product()
    #     result = f"creador_a :\n\tEl código del creador_a a funcionado con: {producto_a.show_data()}"
    #     return result


class ConcreteCreatorB(Creator):
    def create_product(self):
        return ConcreteProductB()

#### INTERFAZ COMÚN DE PRODUCTOS ####


class IProduct(ABC):
    @abstractmethod
    def show_data():
        pass

#### CLASES DE PRODUCTOS CONCRETOS ####


class ConcreteProductA(IProduct):
    def show_data(self):
        return "Hola, soy un producto A"


class ConcreteProductB(IProduct):
    def show_data(self):
        return "Hola, soy un producto B"


##### nuevas funciones ######
creador_a = ConcreteCreatorA()
result = creador_a.some_operation()
print(result)

creador_b = ConcreteCreatorB()
result = creador_b.some_operation()
print(result)
