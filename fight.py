from hero import Hero
from enemy import Enemy


class Fight:
    def __init__(self, hero, enemy):
        self._hero = hero
        self._enemy = enemy

# mai ne trqbva da pisha ot konzolata s kakvo da atakuvam a trqbva da vzimam tova s poveche ataka ako sme edin do drug ili ako sme daleche s spell
    def start_fight(self):
        print ("A fight is started between {} and {}".format(
            self.hero, self.enemy))
        while True:
            atack_with = input("Atack with(weapon or spell): ")

            if atack_with == 'weapon':
                self._enemy.take_damage(self._hero.atack(atack_with))
                print ("Hero casts a {}, hits enemy for {} dmg. Enemy health\
 is {}".format(self._hero.weapon.get_weapon_name(), self._hero.weapon.get_damage(
                ), self._enemy.get_health()))

            elif atack_with == 'spell':
                self._enemy.take_damage(self._hero.atack(atack_with))
                print ("Hero casts a {}, hits enemy for {} dmg. Enemy health\
 is {}".format(self._hero.spell.get_spell_name(), self._hero.spell.get_damage(
                ), self._enemy.get_health()))

            if self._enemy.is_alive() is False:
                print('Enemy is dead')
                return 0

            self._hero.take_damage(self._enemy.atack(atack_with))
            print("Enemy hits hero for {} dmg. Hero health is {}".format(
                self._enemy.get_damage(), self._hero.get_health()))

            if self._hero.is_alive() is False:
                print ("Hero is dead!")
                return False
