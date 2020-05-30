init -290 python:

    register_plugins(
        title="RDS - Ramen Debug Screens",
        version="2.0",
        author="tacoen",
        author_url='https://github.com/tacoen/reramen',
        desc="Ramen Debug/Developer Screens. (Build=False)",
        build=False
    )

    rds = ramen_object()

    rds.kdict('pos',
              panel=[
                  0,
                  0,
                  config.screen_width,
                  config.screen_height,
                  None,
                  '#012'],
              topbar=[0, 0, config.screen_width, 40, (8, 8, 8, 8), '#345'],
              side=[0, 41, 300, config.screen_height -
                    41, (8, 8, 8, 8), '#234'],
              win=[301, 41, config.screen_width - 301,
                   config.screen_height - 32, (8, 8, 8, 8)]
              )

    rds.menu = ramen.objects
    rds.menu['tools'] = ['md']
    rds.menu['tools'].append('plugins')
    rds.menu['tools'].append('icons')

    rds.md_path = "E:/pp-renpy/ramen/wiki/"
    rds.game_path = "E:/pp-renpy/ramen/game/"
    
    rds.report = True

init -79 python:

    def collector(what, obj_type_like):
        res = []
        for g in globals():
            if isinstance(globals()[g], type(globals()[obj_type_like])):
                res.append(g)

        try:
            ramen.objects[what]
        except BaseException:
            ramen.objects[what] = []

        ramen.objects[what] = res

    def rtextformat(var, step=-1, pre='\n', res=''):

        step += 1
        tes = object()

        #res += "*"+str(type(var))+"*"
        if var == {}:
            res += "{color=#666}empty_hash{/color}"

        if var == '':
            res += "{color=#666}empty{/color}"

        if isinstance(var, (type({}), type(tes.__dict__))):
            for v in var:
                res += pre + v + ' {space=10}={space=10} ' + \
                    rtextformat(var[v], step, '\n')

        elif isinstance(var, type(rtextformat)):
            res += "{color=#d0d}" + str(repr(var)) + "{/color}"

        elif isinstance(var, bool):
            if var:
                color = '#0D0'
            else:
                color = '#D00'
            res += "{color=" + color + "}" + repr(var) + "{/color}"

        elif isinstance(var, NoneType):
            res += "{color=#ccc}" + str(var) + "{/color}"

        elif isinstance(var, (int)):
            res += "{color=#f93}" + str(var) + "{/color}"

        elif isinstance(var, (str, unicode)):
            hcolor = ''
            if var.startswith('#'):
                hcolor = "{color=" + var + "}[THIS]{/color}"

            res += "{color=#ff0}" + str(var) + "{/color} " + hcolor

        elif isinstance(var, (tuple, type([]))):
            r = ''
            nn = ''
            if step > 0:
                nn = "\n"

            for v in var:
                if isinstance(v, (int, str, unicode)):
                    ve = str(v)
                else:
                    ve = repr(v)

                r += nn + \
                    "{color=#999}" + str(var.index(v)) + \
                    '{/color} = {color=#9CF}' + ve + '{/color}\n'
                nn = ""

            r = re.sub(r'\s+$', '', r)

            res += r

        else:
            var = repr(var).replace('{', '').replace('}', '')
            res += "{color=#ccc}" + str(repr(var)) + "{/color}"

        return res

    style['rds'] = Style('empty')
    style['rds_text'].font = pt.font_ui_text
    style['rds_text'].size = 20

    style['rds_button_text'] = Style('rds_text')

    style['rds_icon'] = Style('button')
    style['rds_icon'].background = None
    style['rds_icon'].padding = (0, 0, 0, 0)
    style['rds_icon_text'] = Style('ramen_icon_text')
    style['rds_icon_text'].size = 20
    style['rds_icon_text'].line_leading = 4

    style['rds_label'] = Style('rds_text')
    style['rds_label'].bold = True

    style['rds_field'] = Style('rds_text')
    style['rds_field'].color = "#9ab"
    style['rds_field'].text_align = 1.0

    for p in rds.pos:

        style['rds_' + p] = Style('empty')
        style['rds_' + p].xpos = rds.pos[p][0]
        style['rds_' + p].ypos = rds.pos[p][1]
        style['rds_' + p].xsize = rds.pos[p][2]
        style['rds_' + p].ysize = rds.pos[p][3]
        try:
            if rds.pos[p][4] is not None:
                style['rds_' + p].padding = rds.pos[p][4]
        except BaseException:
            pass
        try:
            if rds.pos[p][5] is not None:
                style['rds_' + p].background = rds.pos[p][5]
        except BaseException:
            pass
