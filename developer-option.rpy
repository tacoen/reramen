init -302 python:

    # Set True for developer options
    RAMEN_DEV = True
    
init python:

    if renpy.has_screen('ramen_dev_screen'):    
        config.overlay_screens.append("ramen_dev_screen")
