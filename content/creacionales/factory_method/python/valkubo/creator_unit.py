#### Clase creadoraabstracta ####
from interface_unit import Iunit
from abc import ABC, abstractclassmethod


class CreatorUnit(ABC):
    @abstractclassmethod
    def creator_unit():
        return Iunit()

    def unit_add(self):
        unit = self.creator_unit()
        return f"{unit.name} fue desplegado..."
