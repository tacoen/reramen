init -200 python:

    class inventory(ramen_object):

        def load(self):
            self.__dict__['inventory'] = {}
            pass

        def __call__(self):
            return self.__dict__['inventory']

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
            if dict:
                return self.__dict__['inventory'][item_id].__dict__
            else:
                return self.__dict__['inventory'][item_id]

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
                append = True
            except BaseException:
                self.__dict__['inventory'][item.id] = item.copy()
                self.__dict__['inventory'][item.id].icon = item.icon()
                append = False

            if append:

                self.__dict__['inventory'][item.id].count += item.count

                if item.price != ramen.defvalue['price']:
                    self.__dict__['inventory'][item.id].price = item.price

            return True
