# Pokémon Stats Card Generator

#### Video Demo:  (https://youtu.be/y4uoEnPeKWU)



## Description:
#### Pokemon Stats Card Generator is a python program that will generate an 800x510 .png file that features an official picture of the chosen pokemon and also displays the pokemon's base stats from the video games. The program makes use of the PokéAPI found at https://pokeapi.co/. This is a free, open-source API that contains extensive data from the Pokémon video games.

# How to use:

-   ### From the terminal, run 'python project.py x', where 'x' is the name of the pokémon that a stats card will be generated of.

# Files included:

1. ## project.py

    - #### project.py is the main program of Pokémon Stats Card Generator, containing all of the code and logic to generate a stats card.

2. ## test_project.py

    - #### test_project.py contains several unit tests to test the correct operation of several functions in project.py.

3. ## requirements.txt

    - #### Contains the command to install the PIL module, as per CS50P final project instructions.

# File output

#### Successfully running project.py will generate a .png in the ../project/ directory with the name "pokémon_image.png" where "pokémon" is the name of the pokémon used to generate the card. Several other images such as the art of the pokémon on it's own and the background image are generated, however these are handled by using the 'os.remove' method to avoid excess, unwanted files building up in the project directory.

# Design Choices

#### I wanted a project that I could use API calls and OOP. Originally project.py did not use a Pokemon class. It was structured mostly around many functions, which quickly got cluttered. I decided to change to a class-based approach to reinforce was was learned from the course as pokémon all have same characteristics such as HP, ATK, DEF, etc, which lends itself perfectly to using a class instance for each.

#### Once I discovered that the PokéAPI contained various pokémon sprites, I decided to generate some kind of image using these sprites. Originally I wanted to use the Python PDF module to manipulate the images, as was used during CS50P, however I quickly found out that the Python Image Libray (PIL) was much easier to manipulate and combine the images so this was used instead.

####

# Future Improvements

1. #### More command line arguments modifiers could be used. Some modifiers could be to generate a card from a random Pokémon, different backgrounds or even large cards featuring multiple Pokémon.

2. #### Different backgrounds based on the typing of the Pokémon. Water based background for water pokémon, rocky background for rock pokémon, etc.

3. #### A selector to choose what game sprite to use for the art used on the card.

