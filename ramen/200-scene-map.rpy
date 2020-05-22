init -201 python:
        
    def scene_map(obj,scene_img):
        #renpy.hide_screen('scene_map')
        renpy.show_screen('scene_map',obj=obj,scene_img=scene_img)
        

screen scene_map(obj,scene_img):

    #t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    #a =zip(t[::2], t[1::2])
    # ip a[1]: print a[2]

    python:
        if isinstance(obj,(unicode,str)):
            obj = globals()[obj]
    
        map = obj.map
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
    
    for b in map[scene_img].branch():
        
        python:
            wp = map[scene_img]
            
            img_hover = False
            img = False
            
            if '-hover' in wp.img(b):
                img_hover = wp.img(b)
            else:
                img = wp.img(b)
                
            if img:
                img_hover = im.MatrixColor(img, im.matrix.brightness(0.3))
            if img_hover:
                img = im.MatrixColor(img_hover, im.matrix.opacity(0.0))

        if wp.func(b):
            imagebutton pos wp.pos(b):
                action wp.func(b)
                idle img
                hover img_hover