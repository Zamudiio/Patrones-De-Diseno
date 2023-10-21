from creator_unit import CreatorUnit
from concrete_rifleman_unit import RiflemanUnit


class CreatorRiflemanUnit(RiflemanUnit):
    def creator_unit():
        return RiflemanUnit()
