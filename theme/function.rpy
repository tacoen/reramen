init -10:

    define character.sysd=Character( "sysd", dynamic=True)
        
init -299 python:

    ramen.phone_ui=False
    
    def ramen_notify(message,icon='alert'):
        renpy.show_screen('ramen_notify',message=message,icon=icon)
        
    def dialog_input(prompt,default_value=None,size=(380,150)):
        res=False
        res=renpy.call_screen('input_dialog',prompt=prompt,default_value=default_value,size=size)
        return res
        #renpy.say("sysd",str(res))
        
    class ramen_ui_tool():
    
        def button(self,color,border=Borders(3,1,1,3),black=False):
            if black:
                res=pe.theme_path+'gui/button-frame-black.png'
            else:
                res=pe.theme_path+'gui/button-frame-white.png'
            
            size=renpy.image_size(res)
            img=Composite( size,(0,0),Solid(color),(0,0) ,res )
            return Frame(img,border,tile=False)

        def button_frame(self,color,border=Borders(3,1,1,3),flip=False):

            res=pe.theme_path+'gui/button-frame.png'
            size=renpy.image_size(res)
            if flip:
                res=im.Flip( pe.theme_path+'gui/button-frame.png', True, True)
            
            img=Composite( size,(0,0),Solid(color),(0,0) ,res )
            return Frame(img,border,tile=False)

        def button_underline(self,color):
            fimg=Composite( (24,2),(0,0),Solid(color) )
            img= Composite((24,24),(0,0),Solid('#0000'),(0,22), fimg)
            return Frame(img,Borders(1,1,1,4),tile=False)
        
        def metro_button(self,color,shcolor):
            simg=Composite( (53,53),(0,0),Solid(shcolor) )
            fimg=Composite( (48,48),(0,0),Solid(color) )
            img= Composite((53,53), (5,5), simg,(0,0), fimg)
            return Frame(img,Borders(6,6,6,6),tile=False)
            
        def metro_pad(self,x):
            return (x*2,x*1,x*3,x*2)

    rui= ramen_ui_tool()
