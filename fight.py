from hero import Hero
from enemy import Enemy


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def __str__(self):
        return 'Hero(health{}, mana{}) and Enemy({}, {}, {})'.format(hero.health, hero.mana, enemy.health, enemy.mana, enemy.damage)

    def hero_atack(self, by=''):
        print('A fight is started between our Hero(health{}, mana{}) and Enemy({}, {}, {})'.format(hero.health, hero.mana, enemy.health, enemy.mana, enemy.damage))
        if by == 'spell':
            while hero.is_alive or enemy.is_alive:
                hero_damage = hero.atack('spell')
                enemy.take_damage(hero_damage)
                print('Hero cast {spell.name}, hits enemy for {hero_damage}. Enemy health is {enemy.get_health}'.format(spell.name, hero_damage, enemy.get_health))
                
