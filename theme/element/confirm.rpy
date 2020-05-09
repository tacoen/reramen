screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.

    add ramu.ezfile2(pt.overlays)
    
    modal True
    zorder 200
    layer "dialog_layer"
    style_prefix "dialog"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "dialog_prompt"
                xalign 0.0

            hbox:
                xalign 1.0
                spacing 24
                textbutton _("No") action no_action
                textbutton _("Yes") action yes_action 

    ## Right-click and escape answer "no".
    key "game_menu" action no_action