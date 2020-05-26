init -201 python:

    ramen.events = object()
    
    class ramen_event(object):
    
        def __init__(self, id, **kwargs):

            for k in kwargs:
                self.__dict__[str(k)] = kwargs[k]

            self.__dict__['id'] = id
            
        def __call__(self):
            return self.__dict__
        
        def set(self,key,value):
            self.__dict__[key] = value
        
        def get(self,key):
            try: return self.__dict__[key]
            except: return None
            
        def __setattr__(self,key,value):
            self.set(key,value)
            
        def __getattr__(self,key):
            return self.get(key)
            
        
        def occur(self):
            n = -1
            occur=[]
            
            if self.label is not None: n +=1
            if self.time_cond is not None: n +=1
            if self.has is not None: n +=1
            if self.after is not None: n +=1
            
            if n==-1: return False
                
            for x in range(0,n):
                occur.append(False)
                
            if ramen.label_last == self.label:
                    occur[0] = True
            
            if ramentime.cond() == self.time_cond or \
               ramentime.ico() == self.time_cond or \
               ramentime.word() == self.time_cond:
                    occur[1] = True


            if False in occur:
                return False
            else:
                return True
            

    def Event(id):
        """Return item from `ramen.items` by their id."""
        return ramen.events.__dict__[id]
    
    class define_event(object):
    
        def __new__(cls, id=None, *args, **kwargs):

            if id is None:
                id = "event_" + str(ramu.uid())

            id = ramu.safestr(id)
            ramen.events.__dict__[id] = ramen_event(id, **kwargs)    
            
    define_event('coba',label='red',time_cond='night')
    