# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image test = Solid("#ccc")
image test white = Solid("#fff")
image test black = Solid("#000")

define e = Character("Eileen")
define d = Character("Demi",who_color="#39C")
define s = Character("Semi",who_color="#090")


# The game starts here.

label start:

    "Hi! this is a [config.name] unit-test routines."
    "For a first-timer, I'am a narrator, my words is narratting."
    
    scene test
    $ renpy.notify("You see a scene: test.")

    show eileen happy
    
    e "Hi I'am Eileen!"
    e "I'am a defined chraracter. You can call me 'e' in a script"

    scene test black
    $ ramen_notify("Black scene.")

    e "We are doing it in black scene, aren't we?"

    d "I am Demi."
    s "and I'am Semi."
    
    d "We both are "
    s "Demi and Semi."
    
    scene test white
    $ ramen_notify("White scene. and how well the notification deal with long text like this.",'logo-ramen')
    
    e "We also doing it in white scene."

    scene test

    e 'Lets test the dialogue with a long text.'

    e "This shows a character sprite. A placeholder is used, but you can replace it by adding a file named 'eileen happy.png' to the images directory."

    e "and, You've created a new Ren'Py game."

    menu:
        'option 1':
            e 'Yo select option 1'
        'option 2':
            e 'Yo select option 1'
        'Once you add a story, pictures, and music, you can release it to the world!':
            e "Phew!!!"
        'Release it':
            e "Once you add a story, pictures, and music, you can release it to the world!"


    $ res = dialog_input("Your name")

    "Hi [res]!"
    "The test will be loop after 3, you may check the history layout then."
    "1"
    "2"
    "3"
    "end!"

    jump start
    return
