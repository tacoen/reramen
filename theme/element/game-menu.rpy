## Game Menu screen ######################################################
##
# This lays out the basic common structure of a game menu screen. It's called
# with the screen title, and displays the background, title, and navigation.
##
# The scroll parameter can be None, or one of "viewport" or "vpgrid". When
# this screen is intended to be used with one or more children, which are
# transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    python:
        sf = ramu.ezfind(ramu.safestr(title))
        if sf is None:
            sf = ramu.ezfind('game')

    if sf is not None:
        add sf

    if main_menu:
        add pt.main_menu_background
    else:
        add pt.game_menu_background

    frame:

        hbox:

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    vbox:
        yalign 1.0
        xoffset 24
        yoffset - 32
        style_prefix "navigation"
        use navigation_hbox("Return", Return(), "log-in")

    textbutton ico('close') action Return():
        style 'menu_close_button'
        xalign 1.0
        yalign 0.0

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_frame:
    background "#0006"
    bottom_padding 32

style game_menu_content_frame:
    left_margin 300
    right_margin 20
    top_margin 160

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_label:
    left_padding 300
    ysize 100

style game_menu_label_text:
    font pt.font_label
    size 36
    color "#fff"
    outlines pt.idle_outlines
    yalign 0.5

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is ramen_label
style game_menu_label_text is ramen_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

   # background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True
