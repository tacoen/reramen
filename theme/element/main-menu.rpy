## Main Menu screen ######################################################
##
# Used to display the main menu when Ren'Py starts.
##
# https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    python:

        sf = ramu.ezfind(ramu.str_safe('main'))

        if sf is None:
            sf = ramu.ezfind('game')

    if sf is not None:
        add sf
    else:
        add pt.game_menu_background

    # The use statement includes another screen inside this one. The actual
    # contents of the main menu are in the navigation screen.

    use navigation

    textbutton _("Start") action Start('ramen_newgame'):
        style 'menu_start_button'
        yalign 0.9
        xalign 0.95

    if gui.show_name:

        text "[config.name!t]":
            style "main_menu_title"

        vbox style "version":

            python:
                if ramen.dev:
                    vt = 'DEVELOPER - [config.version]'
                else:
                    vt = '[config.version]'

            text vt style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is ramen_gui
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

style main_menu_title:
    font pt.font_ui_title
    size 60
    xalign 0.95
    yalign 0.2
    color "#fff"

style version:
    xalign 0.95
    yalign 0.15
    spacing 16

style main_menu_version:
    size 20
    font pt.font_ui_text
    color pt.idle_color
