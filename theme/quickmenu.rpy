## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        
        hbox:
            style_prefix "quick"+str(hud.pref)
            xalign 1.0
            yalign 1.0
            spacing 1
            
            textbutton ico('arrow-left') action Rollback()
            textbutton ico('list') action ShowMenu('history')
            textbutton ico('chevron-right') action Skip() alternate Skip(fast=True, confirm=True)
            textbutton ico('chevrons-right') action Preference("auto-forward", "toggle")
            textbutton ico('save') action ShowMenu('save')
            textbutton ico('log-down') action QuickSave()
            textbutton ico('log-up') action QuickLoad()
            textbutton ico('settings') action ShowMenu('preferences')
        

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")