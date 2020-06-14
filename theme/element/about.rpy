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

        vbox:
            spacing 12

            hbox:
                null width 216
                text config.name.title() text_align 0.0 style 'about_title'

            python:
                if gui.about:
                    gui.about.strip()

            hbox:
                null width 216
                text "[gui.about!t]" text_align 0.0

            null height 12

            use hbox_label("Version ", _("[config.version!t]"), 200, 1.0, 0.0)

            null height 12

            use hbox_label("Framework", "Ramen - " + str(ramen_version_name), 200, 1.0, 0.0)

            if pt.about:
                python:
                    credit = ''
                    for a in pt.about:
                        credit += a+"\n"

                    credit = credit.rstrip('\n')

                use hbox_label("Theme", credit, 200, 1.0, 0.0)

            null height 24

            use hbox_label("License", "[renpy.license!t]", 200, 1.0, 0.0)

            hbox:
                null width 216
                text _("Made with {icon=logo-renpy} {a=https://www.renpy.org/}{ui}Ren'Py{/ui}{/a} [renpy.version_only].")

style theme_credit is default
style theme_credit_text:
    size 18

style about_text is ramen_gui:
    size 20

style about_title:
    size 32
    font pt.font_ui_title

style about_label is ramen_label
style about_label_text is ramen_label_text:
    size 20
