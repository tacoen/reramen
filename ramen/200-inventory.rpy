init -200 python:

    class inventory(ramen_object):

        def __init__(self,id=None,*agrs,**kwargs):
            self.makeid(id)
            self.kdict(None, **kwargs)
            self.__dict__['inventory'] = {}
            if self.name is None:
                self.name = self.id.title()

        def __call__(self):
            return self.__dict__['inventory']
            
        def cart(self,item,add=True):

            try: ramen.cart
            except: ramen.cart={}
            
            try: ramen.cart[self.id]
            except: ramen.cart[str(self.id)]=[]
            
            if not add:
                return ramen.cart[self.id]
            else:
                ramen.cart[self.id].append(item)
                

        def use(self, item_id):
            """
            Use will return 3 state in array

            - effect
            - deduced
            - depleted

            """
            res = [False, False, False]

            item = self.__dict__['inventory'][item_id]

            if item.effect is not None:
                what = item.effect[0]
                value = item.effect[1]
                mc.stat[what] = ramu.limits(self, mc.stat[what] + value)
                res[0] = True

            if not item.persist:
                item.count -= 1
                res[1] = True

            if item.count <= 0:
                del self.__dict__['inventory'][item_id]
                res[2] = True

            return res

        def item(self, item_id, dict=False):
            
            mitem = copy.copy(self.__dict__['inventory'][item_id])
            
            for m in pe.itemd:
                try: mitem.__dict__[m]
                except: mitem.__dict__[m] = pe.itemd[m]
                
            mitem.icon = item(item_id).icon()
            
            if dict:
                return mitem.__dict__
            else:
                return mitem

        def has(self,item_id):
            if item_id in  self.__dict__['inventory']:
                return True
            else:
                return False
                
        def add(self, item):

            if not isinstance(item, store.itemobject):
                return False

            try:
                self.__dict__['inventory'][item.id]
                self.__dict__['inventory'][item.id].count += item.count
            except:
                self.__dict__['inventory'][item.id]=object()
                self.__dict__['inventory'][item.id].count = item.count


            return True
