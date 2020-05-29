init -200 python:

    class ramen_inventory(ramen_object):

        def __init__(self, id=None, *agrs, **kwargs):
            self.makeid(id)
            self.kdict(None, **kwargs)
            self.__dict__['inventory'] = {}
            if self.name is None:
                self.name = self.id.title()

        def __call__(self):
            return self.__dict__['inventory']

        def cart(self, item, add=True):

            try:
                ramen.cart
            except BaseException:
                ramen.cart = {}

            try:
                ramen.cart[self.id]
            except BaseException:
                ramen.cart[str(self.id)] = []

            if not add:
                return ramen.cart[self.id]
            else:
                ramen.cart[self.id].append(item)

        def drop(self, item_id):
            del self.__dict__['inventory'][item_id]

        def sell(self, item_id, use_ramen=False):
            i = self.__dict__['inventory'][item_id]
            mc.money += i.price
            del self.__dict__['inventory'][item_id]
            res = [False, False, False, None, i.name +
                   " sold for " + str(i.price) + " $"]
            if use_ramen:
                ramen.res = res
            else:
                return res

        def use(self, item_id, use_ramen=False):
            """
            Will return array:

            | index | type | what |
            | --- | --- | --- |
            | 0 | string | item.name/text, None if empty |
            | 1 | boolean | deduced |
            | 2 | boolean | depleted |
            | 3 | tuple | (what,value), False is no effect |

            ``` python
            res = pocket.use('coke', True)

            > ramen.res
            > [ 'fakecola consumed', True, False, ('energy',3) ]
            ```

            """

            res = [None, False, False, False]

            item = self.__dict__['inventory'][item_id]

            if item.eatable:
                act = "consumed"
            else:
                act = "used"

            res[0] = item.name + " " + act

            if item.effect is not None:

                res[3] = tuple()

                for what in item.effect.keys():
                    value = item.effect[what]
                    mc.stat[what] = ramu.limits(mc.stat[what] + value)
                    if res[3] is None:
                        res[3] = (what, mc.stat[what])
                    else:
                        res[3] = res[3] + (what, mc.stat[what])

            if not item.persist:
                item.count -= 1
                res[1] = True

            if item.count <= 0:
                del self.__dict__['inventory'][item_id]
                res[2] = True

            if use_ramen:
                ramen.res = res
            else:
                return res

        def item(self, item_id, dict=False):

            mitem = copy.copy(self.__dict__['inventory'][item_id])

            for m in pe.itemd:
                try:
                    mitem.__dict__[m]
                except BaseException:
                    mitem.__dict__[m] = pe.itemd[m]

            mitem.icon = item(item_id).icon()

            if dict:
                return mitem.__dict__
            else:
                return mitem

        def has(self, item_id):
            if item_id in self.__dict__['inventory']:
                return True
            else:
                return False

        def add(self, item):

            if not isinstance(item, store.ramen_item):
                return False

            if len(self.inventory.keys()) >= self.max:
                return False

            try:
                self.__dict__['inventory'][item.id]
                self.__dict__['inventory'][item.id].count += item.count
            except BaseException:
                self.__dict__['inventory'][item.id] = item.copy()
                self.__dict__['inventory'][item.id].count = item.count

            return True

        def transfer(self, item_id, dst_id):

            item = self.item(item_id)
            dst = globals()[dst_id]
            dst.inventory[item_id] = item
            self.drop(item_id)
