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

    label .menus:

        menu:
            "Dialog":
                "For a first-timer, I'am a narrator."
                show eileen at center
                e "Hi I'am Eileen!"
                show demi at left
                d "I'am Demi."
                show semi at right
                s "I'am Semi."
                e "Demi is D, and I am E."
                hide demi
                e "Bye Demi!"
                hide semi
                e "So long Semi!"

            "Input":
                "Let's try Input with modal screen"
                $ res = modal_input(prompt="Your name", default=mc.name, size=(380, 150), padding=(16, 16, 16, 32))
                "Hi [res]!"

            "Notify":
                $ renpy.notify("You see gui.about")
                "[gui.about]"
                $ notify_ico("renpy license")
                "[renpy.license]"

            "Next":
                jump .after

    jump .menus

    label .after:

        scene test
        e "Let's create some Ren'Py game."
        scene test black
        e "We are doing it in black scene, aren't we?"
        scene test white
        $ notify_ico("White scene. and how well the notification deal with long text like this.", 'logo-ramen')
        e "We also doing it in white scene."
        scene test
        e 'Lets test the dialogue with a long text.'
        e "This shows a character sprite. A placeholder is used, but you can replace it by adding a file named 'eileen happy.png' to the images directory."

    "The test will be loop after 3, you may check the history layout then."
    "1"
    "2"
    "3"
    "end!"

    jump start

    return
