## Quick Menu screen #####################################################
##
# The quick menu is displayed in-game to provide easy access to the out-of-game
# menus.

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        mousearea:
            area(0, config.screen_height - 41, config.screen_width, 40)
            hovered[Show('quick_menubar')]
            unhovered[Hide('quick_menubar')]

screen quick_menubar():

    hbox:
        at FadeInterval(0.5)
        add(pe.theme_path + 'gui/bottom-shade.png')
        xalign 1.0
        yalign 1.0

    hbox:
        at FadeInterval(0.8)
        style_prefix "quickmenu"
        xalign 1.0
        yalign 1.0
        yoffset - 16
        spacing 8

        default qmtt = Tooltip("")

        textbutton ico('key-back') action Rollback() hovered qmtt.action('Back')
        textbutton ico('key-pause') action ShowMenu('history') hovered qmtt.action('History')
        textbutton ico('key-forward') action Skip() alternate Skip(fast=True, confirm=True) hovered qmtt.action('Skip')
        textbutton ico('key-play') action Preference("auto-forward", "toggle") hovered qmtt.action('Auto')
        textbutton ico('folder') action ShowMenu('save') hovered qmtt.action('Save')
        textbutton ico('folder-qsave') action QuickSave() hovered qmtt.action('Q Save')
        textbutton ico('folder-qload') action QuickLoad() hovered qmtt.action('Q Load')
        textbutton ico('ico-settings') action ShowMenu('preferences') hovered qmtt.action('Pref.')

        null width 8

    if not qmtt.value == "":
        use tooltip(qmtt.value)

style quickmenu is default

style quickmenu_button is button:
    padding(8, 8, 8, 8)

style quickmenu_button_text is ramen_icon_text:
    font pt.font_ui_ico
    size 20
    color pt.idle_color
    hover_color Color(pt.idle_color).tint(.7)
    selected_color Color(pt.idle_color).shade(.7)
    insensitive_color Color(pt.idle_color).opacity(.3)
    outlines pt.idle_outlines
    hover_outlines pt.hover_outlines
    insensitive_outlines pt.insensitive_outlines

# This code ensures that the quick_menu screen is displayed in-game, whenever
# the player has not explicitly hidden the interface.

init python:

    quick_menu = True
    config.overlay_screens.append("quick_menu")
