from creator_unit import CreatorUnit
from concrete_footman_unit import FootmanUnit


class CreatorFootmanUnit(CreatorUnit):
    def creator_unit(self):
        return FootmanUnit()
