init python:

    def showimg(img=False):
        if img:
            renpy.show_screen('showimg',img=img)
        else:
            renpy.hide_screen('showimg')

screen showimg(img):
    add img xalign 0.5 yalign 0.5
    
    