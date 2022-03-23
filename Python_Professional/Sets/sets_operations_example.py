# MIT License

# Copyright (c) 2022 [FacuFalcone]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

pokemon_fire_type = {'Charizard', 'Moltres'}
pokemon_flying_type = {'Charizard', 'Butterfree', 'Pidgeot', 'Fearow', 'Dodrio', 'Gyarados', 'Aerodactyl',
                       'Articuno', 'Zapdos', 'Moltres', 'Dragonite'}
pokemon_venom_type = {'Butterfree'}
pokemon_normal_type = {'Pidgeot', 'Fearow', 'Dodrio'}
pokemon_water_type = {'Gyarados'}
pokemon_rock_type = {'Aerodactyl'}
pokemon_ice_type = {'Articuno'}
pokemon_electric_type = {'Zapdos'}
pokemon_dragon_type = {'Dragonite'}

my_set1 = pokemon_fire_type | pokemon_water_type
print(f'Pokemon fire | water type: {my_set1}')

my_set2 = pokemon_normal_type & pokemon_flying_type
print(f'Pokemon normal & flying type: {my_set2}')

my_set3 = pokemon_flying_type - pokemon_fire_type
print(f'Pokemon flying - fire type: {my_set3}')

my_set4 = pokemon_dragon_type ^ pokemon_electric_type
print(f'Pokemon dragon ^ electric type: {my_set4}')

# *## We can use the difference operator to subtract two or more sets:
my_set5 = pokemon_flying_type - pokemon_venom_type - \
    pokemon_rock_type - pokemon_dragon_type - pokemon_normal_type
print(f'Pokemon flying - venom - rock - dragon - normal type: {my_set5}')
