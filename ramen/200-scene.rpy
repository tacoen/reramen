init -200 python:

    class scene(ramen_extendable):

        def init(self,id=None,*args,**kwargs):
            self.define_byfile()
            
 
        def define_byfile(self):
            
            tdir=[]
            for d in self.dir:
                tdir.append(d+'scene')

            condition = sorted(list(dict.fromkeys( pe.time_cond + pe.time_word  +  pe.time_ico)))
            cond=()
            files = ramu.files(tdir,False,pe.ext_img+pe.ext_txt)
            
            res = {}
            
            def est(where,what=None):
                try: res[where]
                except: res[where]={}
                if what is not None:
                    try: res[where][what]
                    except: res[where][what]={}
                

            for f in files:
            
                fn = ramu.file_info(f)
                
                est(fn.path) 
                
                if fn.path == 'scene':

                    if ' ' in fn.name:
                
                        for c in condition:

                            if ' '+c.lower() in fn.name:

                                fnn = fn.name.split(' ')
                                est(fn.path,fnn[0])
                                
                                try: res[fn.path][fnn[0]]['cond']
                                except: res[fn.path][fnn[0]]['cond']=()
                                
                                if c in pe.time_ico:
                                    res[fn.path][fnn[0]]['cond'] +=("ramentime.ico()=='" + c + "'", f)                
                                elif c in pe.time_word:
                                    res[fn.path][fnn[0]]['cond'] +=("ramentime.word()=='" + c + "'", f)                
                                elif c in pe.time_cond:
                                    res[fn.path][fnn[0]]['cond'] +=("ramentime.cond()=='" + c + "'", f)                     
                    else:
                    
                        est(fn.path,fn.name)
                        res[fn.path][fn.name]['main'] = f
                        
                else:
                    res[fn.path][fn.name] = f

            for k in res['scene']:
                try: 
                    res['scene'][k]['cond']
                    res['scene'][k]['cond']+=(True, res['scene'][k]['main'])
                    renpy.image(self.id + " " + k, ConditionSwitch(*res['scene'][k]['cond']))
                    del res['scene'][k]['main']
                    res['scene'][k] = res['scene'][k]['cond']

                except:
                    renpy.image(self.id + " " + k, res['scene'][k]['main'])
                    res['scene'][k] = res['scene'][k]['main']

            for k in res:
                self.__dict__[k]= res[k]


