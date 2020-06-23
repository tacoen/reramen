init -201 python:

    ramen.map_obj = None

    def scene_map(obj, scene_img):
        #renpy.hide_screen('scene_map')
        #renpy.show_screen('scene_map',obj=obj,scene_img=scene_img)
        renpy.show_screen('scene_map')

    renpy.add_layer('hud', below='screens', menu_clear=True)


screen scene_ezmap(buttons):
    for b in buttons:
        python:
            if '-hover' in b[0]:
                b0_hover = b[0]
                b0 = im.MatrixColor(b0_hover, im.matrix.opacity(0.001))
            else:
                b0 = b[0]
                b0_hover =  im.MatrixColor(b[0], im.matrix.brightness(0.1))
        
        imagebutton pos b[1]:
            idle b0
            hover b0_hover
            action b[2]

screen scene_baseimg(obj, scene_img):

    python:
        base = obj.scene[scene_img]
        if isinstance(base, tuple):
            bz = zip(base[::2], base[1::2])
            for n in range(0, len(bz)):
                if not isinstance(bz[n][0], bool):
                    ct = eval(bz[n][0])
                    if ct:
                        base_img = bz[n][1]
                        break
                else:
                    base_img = bz[n][1]
        else:
            base_img = base

        offline = False

        try:
            if scene_img in obj.offline:
                offline = True
        except BaseException:
            pass

    add base_img

    if offline:
        use scene_overlay(obj.overlay['offline'])

screen scene_map():

    python:
        obj = ramen.map_obj

        if not isinstance(obj, ramen_scene):
            obj = globals()[obj]

        scene_img = obj.last_scene

        map = obj.map

    layer 'scenes'

    use scene_baseimg(obj, scene_img)

    for b in sorted(map[scene_img].branch()):

        python:
            wp = map[scene_img]
            img_hover = False
            img_pass = True
            img = False

        if wp.way(b) is not None:

            python:

                if isinstance(wp.img(b), (str, unicode)):

                    if '-hover' in wp.img(b):
                        img_hover = wp.img(b)
                    else:
                        img = wp.img(b)

                if img_hover and not img:
                    img = im.MatrixColor(img_hover, im.matrix.opacity(0.0))
                if img and not img_hover:
                    img_hover = im.MatrixColor(img, im.matrix.brightness(0.3))

                if not img and not img_hover:
                    img_pass = False

            if wp.func(b) is not None and img_pass:
                imagebutton pos wp.pos(b) action wp.func(b):
                    idle img
                    hover img_hover
