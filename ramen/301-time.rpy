init -301 python:

    class ramen_time():
        """
        See: https://docs.python.org/2/library/datetime.html
        See: https://www.w3schools.com/python/python_datetime.asp
        """

        def __init__(self, y=2020, m=1, d=18, h=13, min=0):

            ramen.time =  datetime.datetime(y, m, d, h, min)
            self.start = datetime.datetime(y, m, d, h, min)

        def __call__(self):
            return ramen.time

        # def __getattr__(self, key):
            # res = getattr(self.time, key)
            # if isinstance(res, (int, str, unicode)):
                # return res
            # else:
                # try:
                    # return res()
                # except BaseException:
                    # return res

        def sethour(self, h):
            delta = h - ramen.time.hour 
            return self.adv(delta)

        def adv(self, a=1, block=False):

            ramen.time += datetime.timedelta(hours=a)

            if ramen.time < self.start:
                ramen.time = self.start

            if block:
                renpy.block_rollback()

            return ramen.time

        def nextday(self, a=8, block=True):
            a = a+(24 - ramen.time.hour)

            ramen.time += datetime.timedelta(hours=a)

            if block:
                renpy.block_rollback()

            return ramen.time

        def clock(self):
            return ramen.time.strftime('%H:%M')

        def ico(self, word=True):
            sun = int(float(ramen.time.hour) / 24 * len(pe.time_ico))
            if word:
                return pe.time_ico[int(sun)]
            else:
                return sun

        def cond(self, word=True):
            sun = int(float(ramen.time.hour) / 24 * len(pe.time_cond))
            if word:
                return pe.time_cond[int(sun)]
            else:
                return sun

        def word(self, word=True):
            sun = int(float(ramen.time.hour) / 24 * len(pe.time_word))
            if word:
                return pe.time_word[int(sun)]
            else:
                return sun

        def seed(self, what):
            if what == 'day':
                return ramen.time.strftime('%y%m%d')
            else:
                return ramen.time.strftime('%U%j%H')
