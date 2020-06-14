init -10 python:

    def action_shortcut(shortcuts=False, reverse=False):
        """
        Forget imagemap, use shortcut!

        ``` python
        $ action_shortcut ({
            'Enter Motel':{'icon':'log-in','action':Jump('lovemotel.inside')},
            'Town Map':{'icon':'ico-map','action':Call('townmap')}
        })
        ```

        """

        if not shortcuts:
            renpy.hide_screen('action_shortcut')
        else:
            renpy.show_screen('action_shortcut', shortcuts=shortcuts, reverse=reverse)


transform shader:
    alpha 0.3
    linear 0.5 alpha 1

screen action_shortcut(shortcuts, reverse=False):

    default shade = False
    default reverse = reverse

    if shade:

        if not reverse:
            add ramu.ezfile('theme/gui/left-shade', Color("#0019")) at shader
        else:
            add ramu.ezfile('theme/gui/right-shade', Color("#0019")) at shader

    vbox:
        spacing 8
        if not reverse:
            yalign 0.7
            xalign 0.025
        else:
            yalign 0.7
            xalign 0.95

        for i in shortcuts:
            python:
                s = shortcuts[i]
                s['text']=i

            use shortcut(s['text'], s['action'], s['icon'], reverse=reverse)


screen shortcut(text, action, icon, reverse):

    hbox xsize 300:
        spacing 4
        box_wrap True
        style_prefix 'shortcut'

        if reverse:
            box_reverse True

        textbutton ico(icon) style 'shortcut_icon':
            action action
            xsize 30

        if reverse:

            textbutton text:
                action action
                xsize 260
                text_xalign 1.0
                hovered[SetScreenVariable('shade', True)]
                unhovered[SetScreenVariable('shade', False)]

        else:

            textbutton text:
                action action
                xsize 260
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
    hover_color "#ff0"
    hover_outlines pt.hover_outlines
