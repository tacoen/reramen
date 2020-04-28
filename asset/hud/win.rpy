init -200 python:

    ramen.default['ui'] = {
        'size' : 20,
        'color' : '#fff'
    }
    
    class ramen_ui(ramen_object):

        def load(self, *args, **kwargs):
            pass
            
        def set(self, key, value):
        
            if key.endswith('color'):
                value = ramu.arrayize(value)
            
            super(ramen_object, self).set(key, value)
            
        def dict2style(self):
        
            def default_or(what):
                try: 
                    return self.get(what)
                except:
                    try: return ramen.default['ui'][what]
                    except: return None
                    
            id = self.id
            style[id]=Style('empty')
            
            for p in range(0,self.color):
            
                style[id+str(p)+'_text'].color = self.default_or('size',color[p])
                style[id+str(p)+'_text'].size = self.default_or('size')
                
            
        
    
        def prop2style(self,obj):
        
            id = obj.id
            prop = obj.prop

            style[id+'_icon_text']=Style('ramen_icon')
            
            L = len(prop.bgcolor)
            
            for i in range(0,L):
                style[id+'_nav'+str(i)]=Style('pad8')
                style[id+'_nav'+str(i)].background=Color(prop.bgcolor[i])
                style[id+'_nav'+str(i)].color=Color(prop.bgcolor[i])
                style[id+'_nav'+str(i)+'_text'].color=style[id+'_nav'+str(i)].color
    

screen hud_win(obj):

    default item = None
    default submenu = None
    default title  = obj.name
    default pref = str(hud.pref)
    
    zorder 102
    add Solid('#0009') xpos 0 ypos 0
    modal True

    textbutton "test":
        action SetScreenVariable('item','cart')
        
    if item is not None:
        text str(item)
