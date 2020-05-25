init -201 python:

    ramen.map_obj = None
        
    def scene_map(obj,scene_img):
        #renpy.hide_screen('scene_map')
        #renpy.show_screen('scene_map',obj=obj,scene_img=scene_img)
        renpy.show_screen('scene_map')
        
    renpy.add_layer('hud', below='screens', menu_clear=True)
    
screen scene_baseimg(obj,scene_img):

    python:
        base = obj.scene[scene_img]
        if isinstance(base,tuple):
            bz = zip(base[::2],base[1::2])
            for n in range(0,len(bz)):
                if not isinstance(bz[n][0],bool):
                    ct = eval(bz[n][0])
                    if ct: 
                        base_img = bz[n][1]
                        break
                else:
                    base_img = bz[n][1]
        else:
            base_img = base
                    
    add base_img

    if scene_img in obj.offline:
        use scene_overlay(flat.find('ambient/offline2'))

screen scene_map():

    python:
        obj = ramen.map_obj
            
        if not isinstance(obj,ramen_scene):
            obj = globals()[obj]

        scene_img = obj.last_scene

        map = obj.map
    

    layer 'scenes'
    
    use scene_baseimg(obj,scene_img)
    
        
    for b in map[scene_img].branch():
    
        python:
            wp = map[scene_img]
            img_hover = False
            img = False

        if wp.way(b) is not None:    
        
            python:
       
               if isinstance(wp.img(b),(str,unicode)):
                    if '-hover' in wp.img(b):
                        img_hover = wp.img(b)
                    else:
                        img = wp.img(b)

               if img:
                    img_hover = im.MatrixColor(img, im.matrix.brightness(0.3))
               if img_hover:
                    img = im.MatrixColor(img_hover, im.matrix.opacity(0.0))

            if wp.func(b) is not None:            
                imagebutton pos wp.pos(b) action wp.func(b):
                    idle img
                    hover img_hover

screen scene_overlay(img):
    add img xpos 0 ypos 0