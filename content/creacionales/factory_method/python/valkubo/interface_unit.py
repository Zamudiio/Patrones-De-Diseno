from abc import ABC, abstractclassmethod


class Iunit(ABC):
    @property
    @abstractclassmethod
    def name(self):
        pass

    @abstractclassmethod
    def atack(self):
        pass

    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def skill(self):
        pass
