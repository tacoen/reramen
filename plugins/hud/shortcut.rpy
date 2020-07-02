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
            add ramu.ezfind('left-shade') at shader
        else:
            add ramu.ezfind('right-shade') at shader

    vbox:
        spacing 0
        if not reverse:
            yalign 0.7
            xalign 0.025
        else:
            yalign 0.7
            xalign 0.975

        for i in shortcuts:
            python:
                s = shortcuts[i]
                s['text']=i

            use shortcut(s['text'], s['action'], s['icon'], reverse=reverse)


screen shortcut(text, action, icon, reverse):

    button:
        hbox xsize 300:
            spacing 0
            box_wrap True
            style_prefix 'shortcut'

            if reverse:
                box_reverse True

            text ico(icon) style 'shortcut_icon'

            if reverse:
                text text+"(R)" text_align 1.0 min_width 270
            else:
                text text min_width 270

        action action
        hovered[SetScreenVariable('shade', True)]
        unhovered[SetScreenVariable('shade', False)]


style shortcut_button is button:
    padding(0, 0, 0, 0)

style shortcut_text is ramen_gui:
    outlines pt.insensitive_outlines
    hover_color "#ff0"
    hover_outlines pt.hover_outlines
    size 22

style shortcut_icon is ramen_icon_text:
    hover_color "#ff0"
    outlines pt.insensitive_outlines
    hover_outlines pt.hover_outlines
    size 22
    line_leading 2
