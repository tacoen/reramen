init -201 python:
        
    def scene_map(id,scene_img):
        renpy.hide_screen('scene_map')
        renpy.show_screen('scene_map',obj_id=id,scene=scene)
        

#screen scene_map(obj_id,scene):
#t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
#a =zip(t[::2], t[1::2])

# ip a[1]: print a[2]
