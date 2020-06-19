init -20 python:

    smphone.register('relation',
                     dir=ramu.getdir(),
                     active=True,
                     order=9,
                     stat={
                         'relation': '#c22',
                         'trust': '#fc3',
                         'like': '#93C',
                     }
                     )

    style['smphone_bar'] = Style('bar')
    style['smphone_bar'].ysize = 10

    for s in smphone.apps()['relation']['stat'].keys():
        color = smphone.apps()['relation']['stat'][s]
        style['smphone_bar_' + s] = Style('smphone_bar')
        style['smphone_bar_' + s].thumb = color
        style['smphone_bar_' + s].base_bar = Color(color).tint(0.4)
        style['smphone_bar_' + s].left_bar = color

screen smphone_apps_relation(var, page):

    python:
        app = ramu.makeobj(smphone.apps()['relation'])
        app.width = style['smphone_default_vbox'].xmaximum
        app.bar_width = style['smphone_default_vbox'].xmaximum - \
            (2 * 8) - 96 - 8
        app.minibar_width = style['smphone_default_vbox'].xmaximum - \
            (2 * 8) - 96 - 8

    use smphone_viewport(app.title, app.hcolor):

        vbox:
            spacing 16
            style_prefix "smphone_default"

            for p in sorted(mc.rel.keys()):

                python:

                    profile_pic = ramu.npc(p, 'profile_pic')
                    if profile_pic is None:

                        profile_pic = ramu.ezfind(pt.anonymous_pic)

                if ramu.globalcheck(p):
                    hbox:
                        spacing 8
                        add im.Scale(profile_pic, 96, 96)

                        vbox:
                            spacing 8

                            text ramu.npc(p, 'name') + " " + ramu.npc(p, 'lastname')

                            for s in sorted(app.stat.keys()):
                                python:
                                    try:
                                        val = mc.rel[p][s]
                                    except BaseException:
                                        val = 0

                                vbox:
                                    hbox xfill True xsize app.minibar_width :
                                        text s.title() size 14
                                        text str(val) size 14 xalign 1.0
                                    bar range 20 value val style 'smphone_bar_' + s xsize app.minibar_width

            null height 32
