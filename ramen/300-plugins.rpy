init -299 python:

    ramen.plugins = {}
    
    def plugin(what):
        try:
            return ramen.plugins.__dict__[what].__dict__
        except:
            return False
            
    class register_plugins(object):

        def __new__(self,id=None,*args,**kwargs):

            
            try: 
                kwargs['dir']
            except:
                kwargs['dir'] = ramu.getdir()
            
            if id is None:
                id = ramu.safestr(re.sub(r'.+/','', os.path.dirname(renpy.get_filename_line()[0])))

            try: 
                kwargs['prefix']
            except:
                kwargs['prefix'] = id

            try: 
                kwargs['build']
            except:
                kwargs['build'] = False
            
            try:
                ramen.plugins.__dict__[id]
            except:
                ramen.plugins.__dict__[id]=ramen_object()
            
            for k in kwargs:
                ramen.plugins.__dict__[id].__dict__[k] = kwargs[k]
 