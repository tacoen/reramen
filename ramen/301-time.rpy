init -301 python:

    class ramen_time():
        """
        See: https://docs.python.org/2/library/datetime.html
        See: https://www.w3schools.com/python/python_datetime.asp
        """

        def __init__(self, y=2020, m=1, d=18, h=13, min=0):
            self.time = datetime.datetime(y, m, d, h, min)
            self.start = self.time

        def __call__(self):
            return self.time

        def __getattr__(self, key):
            res = getattr(self.time, key)
            if isinstance(res, (int, str, unicode)):
                return res
            else:
                try:
                    return res()
                except BaseException:
                    return res

        def adv(self, a=1, block=False):
            self.time = self.time + datetime.timedelta(hours=a)
            self.populate()
            if block:
                renpy.block_rollback()
            return self.time

        def nextday(self, a=8, block=False):
            b = 24 - self.time.hour
            self.time = self.time + \
                datetime.timedelta(hours=b) + datetime.timedelta(hours=a)
            self.populate()
            if block:
                renpy.block_rollback()
            return self.time

        def populate(self):
            global seed
            seed = self.time - self.start

        def clock(self):
            return self.time.strftime('%H:%M')

        def ico(self, word=True):
            sun = int(float(self.time.hour) / 24 * len(pe.time_ico))
            if word:
                return pe.time_ico[int(sun)]
            else:
                return sun

        def cond(self, word=True):
            sun = int(float(self.time.hour) / 24 * len(pe.time_cond))
            if word:
                return pe.time_cond[int(sun)]
            else:
                return sun

        def word(self, word=True):
            sun = int(float(self.time.hour) / 24 * len(pe.time_word))
            if word:
                return pe.time_word[int(sun)]
            else:
                return sun
