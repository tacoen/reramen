init -10 python:

    def action_shortcut(shortcuts=False):
        if not shortcuts:
            renpy.hide_screen('action_shortcut')
        else:
            renpy.show_screen('action_shortcut', shortcuts=shortcuts)

screen action_shortcut(shortcuts):

    default shade = False

    if shade:
        add ramu.ezfile(pt.overlays,Color("#0019"))

    vbox:
        yalign 0.7
        xalign 0.025

        for i in shortcuts:
            $ s = shortcuts[i]
            use shortcut(s['text'], s['action'], s['icon'])

screen shortcut(text, action, icon):

    hbox:
        style_prefix 'shortcut'
        textbutton ico(icon) style 'shortcut_icon':
            action action
        textbutton text:
            action action
            hovered[SetScreenVariable('shade', True)]
            unhovered[SetScreenVariable('shade', False)]

style shortcut_icon is ramen_icon
style shortcut_icon_text is ramen_icon_text:
    outlines pt.insensitive_outlines
    hover_outlines pt.hover_outlines
    size 24
    line_leading 4
style shortcut_button is button
style shortcut_button_text is ramen_gui:
    outlines pt.insensitive_outlines
    hover_outlines pt.hover_outlines
