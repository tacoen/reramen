init -190 python:

    ramen.smphone = False

    smphone = ramen_apps('smphone',
                         background=ramu.ezfile(ramu.getdir() + "body", Color("#999")),
                         exit_btn=ramu.ezfile(ramu.getdir() + "btn", Color("#999")),
                         exit_hover_btn=ramu.ezfile(
                             ramu.getdir() + "btn-hover"),
                         wallpaper=ramu.random_files(
                             ramu.getdir() + "wp/", False)
                         )

    style['smphone'] = Style('default')
    style['smphone_window'].background = smphone.background
    style['smphone_window'].xalign = 0.0
    style['smphone_window'].yalign = 0.0
    style['smphone_window'].size = renpy.image_size(smphone.background)

    style['smphone_frame'].background = "#678"
    style['smphone_frame'].pos = (67, 85)
    style['smphone_frame'].size = (327, 550)
    style['smphone_frame'].padding = (0, 0, 0, 0)

    style['smphone_ico_button'] = Style('button')
    style['smphone_ico_button'].xmaximum = 70
    style['smphone_ico_button'].xalign = 0.5

    style['smphone_ico_button_text'] = Style('ramen_gui')
    style['smphone_ico_button_text'].size = 18
    style['smphone_ico_button_text'].color = "#ddd"
    style['smphone_ico_button_text'].hover_color = "#fff"

    style['smphone_clock'] = Style('default')
    style['smphone_clock'].font = pt.font_ui_title
    style['smphone_clock'].size = 48
    style['smphone_clock'].color = "#ddd"

    style['smphone_exitbtn'] = Style('button')
    style['smphone_exitbtn'].pos = (203, 636)

    smphone.spacing = 5
    smphone.icon_size = (70, 70)
    smphone.cols = style['smphone_frame'].size[0] / \
        (smphone.icon_size[0] + (2 * smphone.spacing))
    smphone.rows = 5
    smphone.grid_height = (
        smphone.icon_size[0] + (2 * smphone.spacing)) * smphone.rows
    smphone.init_pos = (67, 85)

    style['smphone_default_text'] = Style('ramen_gui')
    style['smphone_default_text'].color = "#222"
    style['smphone_default_text'].size = 24

    style['smphone_default_vbox'] = Style('vbox')
    style['smphone_default_vbox'].xsize = style['smphone_frame'].size[0] - 32

    style['smphone_default_hbox'] = Style('hbox')
    style['smphone_default_hbox'].xfill = True
    style['smphone_default_hbox'].yalign = 0.0

    style['smphone_default_label_text'] = Style('smphone_default_text')
    style['smphone_default_label_text'].color = "#666"
    style['smphone_default_label_text'].size = 20

    style['smphone_default_button'] = Style('ramen_button_large')
    style['smphone_default_button'].background = "#ccc"
    style['smphone_default_button'].hover_background = "#999"
    style['smphone_default_button'].xalign = 0.5
    style['smphone_default_button'].yalign = 0.5

    style['smphone_default_button_text'] = Style('ramen_gui')
    style['smphone_default_button_text'].color = "#333"
    style['smphone_default_button_text'].hover_color = "#fff"

init -9:

    screen smphone_window():

        window:
            frame pos smphone.init_pos xsize 327 ysize 550 background smphone.wallpaper:
                transclude

    screen smphone_ui():

        default apps = None
        default var = None
        default page = None

        layer 'screens'
        zorder 102
        style_prefix 'smphone'

        use smphone_window():
            if apps is None:
                use smphone_launcher()
            else:

                python:
                    scr = smphone.apps()[apps]['start']
                    if renpy.has_screen(scr):
                        renpy.use_screen(scr, var=var, page=page)
                    else:
                        scr = False

                if not scr:

                    text '404'

        $ smphone_exit_action = [ Hide('smphone_ui'), SetVariable('ramen.smphone', False)]

        key "game_menu" action smphone_exit_action

        imagebutton xpos 203 ypos 636 action smphone_exit_action:
            idle smphone.exit_btn
            hover smphone.exit_hover_btn

    screen smphone_launcher():

        text ramentime.clock() style  'smphone_clock'

        vpgrid id "smphone_launcher":
            ypos style['smphone_frame'].size[1] - smphone.grid_height - 32
            cols smphone.cols
            rows smphone.rows
            spacing smphone.spacing

            for a in sorted(ramen.active_apps['smphone']):

                python:
                    a = re.sub(r'^\d+\:', '', a)
                    app = ramu.makeobj(smphone.apps()[a])

                vbox:
                    spacing 0
                    style_prefix 'smphone_ico'
                    imagebutton action SetScreenVariable('apps', a):
                        idle app.icon
                        hover im.MatrixColor(app.icon, im.matrix.brightness(0.2))
                    textbutton a action SetScreenVariable('apps', a)

    screen smphone_viewport(title, hcolor):

        frame xpos 0 ypos 0 style 'smphone_frame' background "#fff" padding(0, 0, 0, 0):
            vbox:
                frame background hcolor xsize 1.0 ysize 32 padding(4, 4, 4, 4):
                    hbox ysize 32 xfill True:
                        text title size 16
                        textbutton ico('close') style 'ramen_icon':
                            xalign 1.0
                            text_size 20
                            text_line_leading - 2
                            action SetScreenVariable('apps', None)

            viewport id 'smphone_viewport':
                yoffset 40
                xoffset 8
                ysize style['smphone_frame'].size[1] - 56
                xsize style['smphone_frame'].size[0] - 24
                draggable True
                mousewheel True

                transclude

            vbar value YScrollValue('smphone_viewport'):
                ypos 32 xalign 1.0 ysize style['smphone_frame'].size[1] - 48
