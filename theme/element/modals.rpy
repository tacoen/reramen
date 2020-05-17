init python:

    modal = ramen_object()

    pt.modal_background = '#fff'

    style['modal_frame'] = Style('empty')
    style['modal_frame'].background = pt.modal_background
    style['modal_frame'].padding = (16, 16, 16, 16)
    style['modal_frame'].xalign = .5
    style['modal_frame'].yalign = .5
    style['modal_frame'].xsize = config.screen_width / 2
    style['modal_frame'].ysize = config.screen_height / 2

    style['modal_text'] = Style('ramen_tex')
    style['modal_text'].color = ramu.invertColor(pt.modal_background)

    style['modal_prompt'] = Style('ramen_label')
    style['modal_prompt_text'] = Style('ramen_gui')
    style['modal_prompt_text'].color = "#111"
    style['modal_prompt_text'].text_align = 0.0

    style['modal_button'] = Style('button')
    style['modal_button'].background = "#0000"
    style['modal_button'].padding = (8, 4, 8, 4)

    style['modal_button_text'] = Style('ramen_tex')
    style['modal_button_text'].size = 24
    style['modal_button_text'].color = '#26C'
    style['modal_button_text'].hover_color = Color(
    style['modal_button_text'].color).tint(.7)
    style['modal_button_text'].selected_color = Color(
    style['modal_button_text'].color).shade(.7)

    style['modal_closebutton'] = Style('ramen_icon')
    style['modal_closebutton'].xalign = 1.0
    style['modal_closebutton'].yalign = 0.0
    style['modal_closebutton'].yoffset = -style['modal_frame'].top_padding
    style['modal_closebutton'].xoffset = style['modal_frame'].right_padding
    style['modal_closebutton'].background = Color("#c00")
    style['modal_closebutton'].hover_background = Color("#900")

    style['modal_closebutton_text'] = Style('ramen_icon_text')
    style['modal_closebutton_text'].size = 24
    style['modal_closebutton_text'].color = Color("#bbb")
    style['modal_closebutton_text'].hover_color = Color("#fff")

    style['modal_label'] = Style('ramen_label')
    style['modal_label'].yoffset = -style['modal_frame'].top_padding / 2

    style['modal_label_text'] = Style('ramen_label_text')
    style['modal_label_text'].color = ramu.invertColor(pt.modal_background)


    style['modal_vscrollbar'].xsize=8
    style['modal_vscrollbar'].thumb=Color('#999').opacity(.2)
    style['modal_vscrollbar'].base_bar=Color('#ccc').opacity(.9)

    style['modal_vbar']=Style('modal_vscrollbar')
    style['modal_vbar'].xsize=3
    
    def modal_display(**kwargs):
        """
        show `modal_display` screen with keyword arguments.

        ``` python
            $ modal_display(text='show me some text', title='Information',showtitle=True,align=(0.5,0.5)):
        ```
        """

        renpy.show_screen('modal_display', **kwargs)

    def modal_input(**kwargs):
        """
        call `modal_input` screen with keyword arguments.

        ``` python
        $ res = modal_input(prompt="Your name",default=mc.name,size=(380,150),padding=(16,16,16,32))
        e "Hi! [res]."
        ```

        Accepted argument:

        * default = 'string'
        * prompt = 'string'
        * size = (w,h)
        * padding = (l,t,r,b)
        * align = (xpos,ypos)
        * title = 'string'
        * showtitle = False
        * closebutton = True

        """
        res = False
        res = renpy.call_screen('modal_input', **kwargs)
        return res

screen modal(screenname, **kwargs):

    python:
        try:
            showtitle = kwargs['showtitle']
        except BaseException:
            showtitle = True
        try:
            title = kwargs['title']
        except BaseException:
            title = ''

        if title == '':
            showtitle = False

        try:
            closebutton = kwargs['closebutton']
        except BaseException:
            closebutton = True
        try:
            padding = kwargs['padding']
        except BaseException:
            padding = False

        try:
            size = kwargs['size']
        except BaseException:
            size = False
        try:
            align = kwargs['align']
        except BaseException:
            align = False

    add ramu.ezfile2(pt.overlays)

    layer "dialog_layer"
    style_prefix "modal"
    modal True
    

    frame:
        if padding:
            padding padding
        if align:
            align align
        if size:
            xsize size[0]
            ysize size[1]

        if closebutton:
            textbutton ico('close') style 'modal_closebutton' action ToggleScreen(screenname)

        if showtitle:
            label title.title()
            
            hbox yoffset 32:
                transclude
        else:
            transclude


screen modal_display(**kwargs):

    $ text_display = kwargs['text']

    use modal('modal_display', **kwargs):
        style_prefix "modal"
        text text_display


screen modal_input(**kwargs):

    python:
        try:
            default_value = kwargs['default']
        except BaseException:
            default_value = ''
        try:
            prompt = kwargs['prompt']
        except BaseException:
            prompt = "Input:"
        try:
            size = kwargs['size']
        except BaseException:
            size = (
                style['modal_frame'].xmaximum,
                style['modal_frame'].ymaximum)
        try:
            padding = kwargs['padding']
            xin = size[0] - padding[0] - padding[2]
        except BaseException:
            xin = size[0] - style['modal_frame'].left_padding - \
                style['modal_frame'].right_padding

    use modal('modal_input', **kwargs):

        vbox:
            yalign 0.5
            style_prefix "modal"

            label _(prompt):
                style "modal_prompt"
                xalign 0.0

            null height 8
            input default default_value:
                xminimum xin

            add ramu.hline((xin, 1), "#666")

# Confirm

screen confirm(message, yes_action, no_action, timeout=None):

    # Ensure other screens do not get input while this screen is displayed.
    layer 'dialog_layer'
    zorder 200
    
    use modal('confirm',
              closebutton=False, showtitle=False, size=(560, 200), padding=(24, 24, 24, 24), align=(0.5, 0.75)):

        vbox yfill True xfill True:
            style_prefix "modal"
            yalign 0.5

            label _(message):
                yalign 0.5
                xalign 0.0
                style "modal_prompt"

            hbox:
                xalign 1.0
                yalign 1.0
                spacing 24
                textbutton _("No") action no_action
                textbutton _("Yes") action yes_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action
    
    if timeout is not None:
    
        timer timeout action[Hide('confirm'), no_action]
