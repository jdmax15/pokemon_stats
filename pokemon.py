import requests
from PIL import Image, ImageDraw, ImageFont
import sys
import os

# Defines the Pokemon class and instance variables.
class Pokemon:
    def __init__(self, name):
        self.name = name
        self.data = self.get_data()
        self.art_url = self.get_art_url()
        self.stats = self.get_stats()


    # Gets the json file response for the pokemon.
    def get_data(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            sys.exit("Error, pokemon not found")


    # Gets basic info about the pokemon to store as self.stats.
    def get_stats(self):
        if self.data:
            pokemon_data = self.data
            pokemon_info = {
                "name": pokemon_data["name"],
                "height": pokemon_data["height"],
                "weight": pokemon_data["weight"],
                "id": pokemon_data["id"]
            }

            types = pokemon_data.get("types", [])
            types_len = len(types)

            # Assigns the pokemon type, if there are 2 types they are concatenated.
            if types_len > 0:
                pokemon_info['type'] = types[0]['type']['name']
            if types_len > 1:
                pokemon_info['type'] = pokemon_info['type'] + "/" + types[1]['type']['name']

            # Accesses and assigns the RPG stats to the self.stats dict.
            rpg_stats = pokemon_data.get("stats", [])
            pokemon_info['hp'] = rpg_stats[0]['base_stat']
            pokemon_info['atk'] = rpg_stats[1]['base_stat']
            pokemon_info['def'] = rpg_stats[2]['base_stat']
            pokemon_info['spatk'] = rpg_stats[3]['base_stat']
            pokemon_info['spdef'] = rpg_stats[4]['base_stat']

        return pokemon_info


    # Gets the URL for the pokemons official artwork .png file.
    def get_art_url(self):
        if self.data:
            pokemon_art_url = self.data['sprites']['other']['official-artwork']['front_default']
            return pokemon_art_url


    # Downloads and stores the .png file in the directory.
    def download_art(self):
        if self.art_url:
            img = requests.get(self.art_url)
            with open(f"{self.name}_art.png", "wb") as file:
                file.write(img.content)


    # Returns the self.stats if the pokemon class is printed.
    def __str__(self):
        return f"{self.stats['name'].capitalize()}\n\nHeight: {self.stats['height'] * 10}cm\nWeight: {self.stats['weight'] / 10}kg\nID: {self.stats['id']}\nType: {self.stats['type'].capitalize()}\n\nBase Stats\n\nHP: {self.stats['hp']}\nAtk: {self.stats['atk']}\nDef: {self.stats['def']}\nSp. Atk: {self.stats['spatk']}\nSp. Def: {self.stats['spdef']}"


    # Creates the background image.
def generate_bg():
    black_bg = Image.new('RGB', (800, 510), color='grey')
    black_bg.save("black_bg.png")


    # Overlays the pokemon onto the background and saves a new .png.
def combine_imgs(pokemon):
    background = Image.open("black_bg.png")
    overlay = Image.open(f"{pokemon.name}_art.png")
    background.paste(overlay, (0,0), overlay)
    background.save("combined.png")


    # Puts the pokemon stats over the combined image.
def overlay_text(pokemon):
    im = Image.open("combined.png")
    draw = ImageDraw.Draw(im)
    text = f"{pokemon}"
    font = ImageFont.load_default(size=30)
    text_position = (500, 15)
    text_color = (255, 255, 255)
    draw.text(text_position, text, font=font, fill=text_color)
    im.save(f"{pokemon.name}_image.png")


    # Downloads art, overlays onto background, adds stats, removes old images.
def make_final_image(pokemon):
    pokemon.download_art()
    generate_bg()
    combine_imgs(pokemon)
    overlay_text(pokemon)
    os.remove("black_bg.png")
    os.remove("combined.png")
    os.remove(f"{pokemon.name}_art.png")


    # Ensures a pokemon name is entered at the CLI.
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    pokemon_name = sys.argv[1]

    try:
        pokemon = Pokemon(pokemon_name.lower())
    except ValueError:
        sys.exit("Error")

    make_final_image(pokemon)


if __name__ == "__main__":
    main()