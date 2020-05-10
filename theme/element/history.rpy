## History screen ########################################################
##
# This is a screen that displays the dialogue history to the player. While
# there isn't anything special about this screen, it does have to access the
# dialogue history stored in _history_list.
##
# https://www.renpy.org/doc/html/history.html

screen 2history():

    tag menu

    # Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                # This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        # Take the color of the who text from the Character, if
                        # set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")

screen history():

    tag menu

    # Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        vbox:

            for h in _history_list:
                # text repr(h)
                hbox:
                    if h.who:
                        text h.who + ":":
                            style 'history_name'
                            substitute False
                            if "color" in h.who_args:
                                color h.who_args["color"]
                    else:
                        null width 155

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)

                    text what:
                        substitute False

                null height 16

style history_hbox:
    xfill True

style history_name is ramen_label:
    xsize 155
    min_width 155
    text_align 1.0

style history_name_text is ramen_label_text:
    min_width 155
    text_align 1.0
    color pt.idle_color

style history_text is ramen_tex:
    min_width 740
    xsize 740
    text_align 0.0
    size 22
    layout("subtitle" if 0.0 else "tex")
