from interface_unit import Iunit


class FootmanUnit(Iunit):

    @property
    def name(self):
        return "Footman"

    def atack(self):
        return "Estoy atacando con una espada"

    def move(self):
        return "Estoy caminando"

    def skill(self):
        return "Ataque de escudo"
