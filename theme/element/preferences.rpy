## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        hbox:

            vbox:
                xsize 300
                #box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            vbox:
                style_prefix "slider"
                xsize 460

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time") yalign 0.5

                label _("Text Speed")
                bar value Preference("text speed")


                if config.has_music:
                    label _("Music Volume")
                    bar value Preference("music volume")

                if config.has_sound:
                    hbox:
                        label _("Sound Volume")
                        if config.sample_sound:
                            textbutton ico('volume-on') style 'sound_test' action Play("sound", config.sample_sound)

                    bar value Preference("sound volume")

                    if config.has_voice:
                        hbox:
                            label _("Voice Volume")
                            if config.sample_voice:
                                textbutton ico('volume-on') style 'sound_test' action Play("voice", config.sample_voice)

                    
                        bar value Preference("voice volume")

                    if config.has_music or config.has_sound or config.has_voice:
                        null height 32
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style sound_test is button:
    padding (8,24,8,2)
    xalign 1.0

style pref_label is ramen_label:
    top_margin 24
    bottom_margin 2

style pref_label_text is ramen_label_text:
    yalign 0.5


style radio_label is pref_label
style radio_label_text is pref_label_text

style check_label is pref_label
style check_label_text is pref_label_text

style slider_label is pref_label
style slider_label_text is pref_label_text

style slider_slider is ramen_slider:
    xsize 450

style radio_button_text is ramen_gui:
    size 22

style slider_button_text is radio_button_text
style check_button_text is radio_button_text

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style sound_test_text is ramen_icon_text:
    size 20
    line_leading 8
    color pt.idle_color
    hover_color pt.hover_color
    selected_color pt.accent_color

style slider_hbox:
    xfill True
    top_margin 24
