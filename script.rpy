# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image test = Solid("#ccc")
image test white = Solid("#fff")
image test black = Solid("#000")

define e = Character("Eileen")
define d = Character("Demi", who_color="#39C")
define s = Character("Semi", who_color="#090")

# The game starts here.

label start:

    "Hi! this is a [config.name] unit-test routines."

    jump testmenu