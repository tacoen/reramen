init -199 python:

    
    # Constant For Shared Resources
    RAMEN_THEME_PATH = ramu.getdir()

    font = object()
    font.game_text = RAMEN_THEME_PATH+'fonts/WorkSans-Regular.ttf'
    font.game_label = RAMEN_THEME_PATH+'fonts/WorkSans-SemiBold.ttf'
    font.ui_title=RAMEN_THEME_PATH+'fonts/WorkSans-ExtraLight.ttf'
    font.ui_label=RAMEN_THEME_PATH+'fonts/WorkSans-Light.ttf'
    font.ui_text = RAMEN_THEME_PATH+'fonts/Abel-Regular.ttf'
    font.ui_ico = RAMEN_THEME_PATH+'fonts/icon/fonts/ramen-ico.ttf'



# layers
define config.layers = ['master', 'transient', 'ambient', 'screens', 'overlay','console', 'dialog_layer']
    
style ramen_gui is default:
    font font.ui_text
    antialias True
    size 24

style ramen_gui_text is ramen_gui
    
style ramen_icon:
    font font.ui_ico
    antialias True
    size 32

style ramen_icon_text is ramen_icon

##############    

screen inventory_ui():
    text 'dump'
    
    