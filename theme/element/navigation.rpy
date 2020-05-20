## Navigation screen #####################################################

screen navigation_hbox(text, action, icon=None):
    hbox:
        if icon is not None:
            text ico(icon) style 'navigation_icon'
        else:
            null width 32

        textbutton _(text) action action


screen navigation():

    style_prefix "navigation"

    frame:

        if main_menu:
            background ramu.ezfile2(pt.main_side_background, pt.nav_background)
        else:
            background ramu.ezfile2(pt.game_side_background, pt.nav_background)

        vbox:
            yalign 1.0
            spacing 16

            if main_menu:
                use navigation_hbox("New Game", Start('ramen_newgame'))

                if ramen.episode_menu:
                    use navigation_hbox("Episodes", ShowMenu("ramen_episodes_menu"), "menu1")


            else:
                use navigation_hbox("History", ShowMenu("history"))
                if _in_replay:
                    use navigation_hbox("End Replay", EndReplay(confirm=True))
            
            use navigation_hbox("Load", ShowMenu("load"), "folder")

            if not main_menu:
                use navigation_hbox("Save", ShowMenu("save"))

            use navigation_hbox("Preferences", ShowMenu("preferences"), "ico-settings")

            if renpy.variant("pc") or (renpy.variant(
                    "web") and not renpy.variant("mobile")):

                # Help isn't necessary or relevant to mobile devices.
                use navigation_hbox("Help", ShowMenu("help"))

            null height 4

            if not main_menu:
                use navigation_hbox("Main Menu", MainMenu(), "menu1")

            use navigation_hbox("About", ShowMenu("about"), "logo-ramen")

            if renpy.variant("pc"):
                # The quit button is banned on iOS and unnecessary on Android and
                # Web.
                use navigation_hbox("Quit", Quit(confirm=not main_menu), 'log-out2')


style navigation_frame is frame:
    background "#002c"
    xsize 280
    ysize config.screen_height
    xpos 0
    ypos 0
    padding(24, 110)

style navigation_icon is ramen_icon_text:
    size 20
    min_width 32
    text_align 0.5
    line_leading 8
    color Color(pt.idle_color).opacity(.9)

style navigation_button is button
style navigation_button_text is ramen_gui:
    size 24
    color pt.idle_color
    hover_color pt.hover_color
    insensitive_color pt.insensitive_color
