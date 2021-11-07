from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        pokemons_details = ""
        for pokemon in self.pokemons:
            pokemons_details += f" - {pokemon.pokemon_details()}\n"
        # Pokemon Trainer {trainer_name}
        # Pokemon count {the amount of pokemon caught}
        # - {pokemon_details1}
        # ...
        # - {pokemon_detailsN}
        return f"Pokemon Trainer {self.name}\n""" \
               f"Pokemon count {len(self.pokemons)}\n"\
               f"{pokemons_details}"


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# third_pokemon = Pokemon("Snorlax", 200)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(third_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
