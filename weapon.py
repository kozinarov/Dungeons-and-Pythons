class Weapon:
    def __init__(self, name="The Axe of Destiny", damage=20):
        self._name = name
        self._damage = damage


    def get_weapon_name(self):
        return self._name


    def get_damage(self):
        return self._damage

