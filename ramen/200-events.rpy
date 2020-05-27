init -201 python:

    ramen.events = object()
    
    class ramen_event(object):
    
        def __init__(self, id, **kwargs):

            for k in kwargs:
                self.__dict__[str(k)] = kwargs[k]

            self.__dict__[str('id')] = str(id)
            
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
        
        def occur(self,inv=None):

            occur=[]
            
            if self.label is not None: 
            
                if ramen.label_last == self.label:
                    occur.append(True) 
                else:
                    occur.append(False) 
           
            if self.time_cond is not None: 

                if ramentime.cond() == self.time_cond or \
                    ramentime.ico() == self.time_cond or \
                    ramentime.word() == self.time_cond:
                    occur.append(True)
                else:
                    occur.append(False) 
            
            if self.after is not None:

                if ramentime.hour() > self.after:
                    occur.append(True)
                else:
                    occur.append(False) 
            
            if inv is not None:

                if self.has is not None: 
                    if inv.has(self.has):
                        occur.append(True)
                    else:
                        occur.append(False)

            if occur == []:
                return False
            
            if False in occur:
                return False
            else:
                return True

    def Event(id):
        """Return event from `ramen.events` by their id."""
        return ramen.events.__dict__[id]
    
    class define_event(object):
    
        def __new__(cls, id=None, *args, **kwargs):

            if id is None:
                id = "event_" + str(ramu.uid())

            id = ramu.safestr(id)
            ramen.events.__dict__[id] = ramen_event(id, **kwargs)    
            
  
    