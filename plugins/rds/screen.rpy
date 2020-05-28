screen ramen_dev_screen():

    default title = 'Main'
    default obj_type = None
    default obj = None
    default show = False
    
    layer 'console'

    if show:

        modal True
        zorder 105

        frame style 'rds_panel':
            style_prefix 'rds'
            use rds_topbar(title)
            use rds_side(obj_type)
            if obj is not None:
                use rds_win(obj, obj_type)
    else:
        modal False
        textbutton '{icon=logo-ramen}' text_size 24  padding (8,8,8,8):
            action ToggleScreenVariable('show')

screen rds_win(obj, obj_type):

    viewport id 'vp':
        xoffset style['rds_side'].xmaximum + 8
        xsize config.screen_width - style['rds_side'].xmaximum - 8
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True

        style_prefix 'rds'

        if renpy.has_screen('rdsa_' + obj_type + '_' + obj):
            $ renpy.use_screen('rdsa_' + obj_type + '_' + obj)
        elif renpy.has_screen('rdsa_' + obj_type):
            $ renpy.use_screen('rdsa_' + obj_type, obj=obj)
        else:
            use rds_getasset(obj_type=obj_type, obj=obj)

screen rds_getasset(obj_type, obj):

    if obj_type == 'ramen_item':
        $ asset = item(obj)()
    else:
        $ asset = globals()[obj]()

    vbox:
        transclude
        spacing 8

        use rds_dictparam(asset)

        if obj_type == 'npc':
            add ramu.hline((style['rds_win'].xminimum, 2), "#999")
            use rds_dictparam(character.__dict__[obj].__dict__)

        null height 32

screen rds_dictparam(asset):
    for k in sorted(asset.keys()):
        python:
            res = re.sub(r'(^\s+|\+$)', '', rtextformat(asset[k]))
            res = res.strip()

        hbox:
            text k min_width 180 style 'rds_field'
            null width 16
            text res

screen rds_side(obj_type):

    frame style 'rds_side':
        style_prefix 'rds'

        vbox:

            use rds_side_menuitem('tools', obj_type)

            for t in rds.menu:

                if not t == 'tools':
                    use rds_side_menuitem(t, obj_type)

screen rds_side_menuitem(t, obj_type):

    python:

        if t.startswith('ramen_'):
            st = t.replace('ramen_', '')
        else:
            if t == 'tools':
                st = 'Ramen Dev Tools'
            else:
                st = t

        if obj_type == t:
            this_icon = 'square-minus'
            this_action = [
                SetScreenVariable(
                    'obj_type', None), SetScreenVariable(
                    'obj', None)]
        else:
            this_icon = 'square-plus'
            this_action = [
                SetScreenVariable(
                    'obj_type', t), SetScreenVariable(
                    'obj', None)]

    hbox xfill True:
        style_prefix 'rds'
        textbutton st:
            action this_action
        textbutton ico(this_icon) style 'rds_icon' xalign 1.0:
            action this_action

    if obj_type == t:
        use rds_obj_child(t)

screen rds_obj_child(obj_type):

    if obj_type is not None:

        vbox xoffset 24:
            for t in ramen.objects[obj_type]:
                textbutton t action SetScreenVariable('obj', t)

screen rds_topbar(title):

    frame style 'rds_topbar':
        style_prefix 'rds'
        hbox xfill True:
            text 'Ramen Dev: ' + title.title() style 'rds_label'
            textbutton ico('square-x') style 'rds_icon' xalign 1.0:
                action ToggleScreenVariable('show')

init python:
    config.overlay_screens.append("ramen_dev_screen")
