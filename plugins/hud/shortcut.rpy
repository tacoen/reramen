init -10 python:

    def action_shortcut(shortcuts=False):
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
            renpy.show_screen('action_shortcut', shortcuts=shortcuts)

transform leftshade:
    alpha 0.3
    linear 0.5 alpha 1

screen action_shortcut(shortcuts):

    default shade = False

    if shade:
        add ramu.ezfile('theme/gui/left-shade', Color("#0019")) at leftshade

    vbox:
        yalign 0.7
        xalign 0.025
        spacing 24

        for i in shortcuts:
            python:
                s = shortcuts[i]
                s['text']=i

            use shortcut(s['text'], s['action'], s['icon'])

screen shortcut(text, action, icon):

    hbox:
        spacing 8
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
    hover_color "#ff0"
    hover_outlines pt.hover_outlines
