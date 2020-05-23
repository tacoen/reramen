## About screen ##########################################################
##
# This screen gives credit and copyright information about the game and Ren'Py.
##
# There's nothing special about this screen, and hence it also serves as an
# example of how to make a custom screen.

screen about():

    tag menu

    # This use statement includes the game_menu screen inside this one. The
    # vbox child is then included inside the viewport inside the game_menu
    # screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        label "[config.name!t]"
        vbox:
            spacing 2
            text _("Version [config.version!t] - [build.name!t]")
            python:
                if gui.about:
                    gui.about.strip()

            text "[gui.about!t]"

        if pt.about:

            label _("Ramen Theme")
            vbox:
                spacing 2
                style 'theme_credit'
                for credit in pt.about:
                    text credit

        vbox:
            null height 8
            text _("Made with {icon=logo-renpy} {a=https://www.renpy.org/}{ui}Ren'Py{/ui}{/a} [renpy.version_only].")
            null height 16
            add ramu.hline((900, 1), "#fff6")
            null height 8
            text _("[renpy.license!t]")

style theme_credit is default
style theme_credit_text:
    size 18

style about_text is ramen_gui:
    size 20

style about_label is ramen_label
style about_label_text is ramen_label_text:
    size 20
