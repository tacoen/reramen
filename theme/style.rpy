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

init -199:
    
    image white = Solid('#fff')
    image black = Solid('#000')
    
    style antialias is default:
        antialias True

    style ramen_label is antialias:
        font font.ui_label
        
    style ramen_gui is antialias:
        font font.ui_text
        size 24

    style ramen_gui_text is ramen_gui
    
    style ramen_icon is antialias:
        font font.ui_ico
        size 32

    style ramen_icon_text is ramen_icon

    style pad16 is empty:
        padding (16,16,16,16)
    
    style pad8 is empty:
        padding (8,8,8,8)

    style pad4 is empty:
        padding (4,4,4,4)
        
    style pad2 is empty:
        padding (2,2,2,2)


##############    

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Color("#fff").opacity(.3)
    thumb Color("#fff").opacity(.6)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Color("#fff").opacity(.3)
    thumb Color("#fff").opacity(.6)

    
    