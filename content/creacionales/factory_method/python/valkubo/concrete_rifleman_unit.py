from interface_unit import Iunit


class RiflemanUnit(Iunit):
    @property
    def name(self):
        return "Fusilero"

    def atack(self):
        return "Estoy disparando"

    def move(self):
        return "Estoy caminando"

    def skill(self):
        return "Usando HeadShot"


# fusilero1 = RiflemanUnit()
# fusilero1.atack()
