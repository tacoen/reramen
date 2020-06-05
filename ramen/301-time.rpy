init -301 python:
    
    
    class ramen_time():
        """
        See: https://docs.python.org/2/library/datetime.html
        See: https://www.w3schools.com/python/python_datetime.asp
        """

        def __init__(self, y=2020, m=1, d=18, h=13, min=0):
            
            ramen.time =  datetime.datetime(y, m, d, h, min)
            self.time = ramen.time
            self.start = datetime.datetime(y, m, d, h, min)

        def __call__(self):
            return self.time

        def sync(self):
            self.time = ramen.time
            
        def __getattr__(self, key):
            res = getattr(self.time, key)
            if isinstance(res, (int, str, unicode)):
                return res
            else:
                try:
                    return res()
                except BaseException:
                    return res

        def sethour(self, h):
            delta = h - self.hour
            self.adv(h)
            return self.time

        def adv(self, a=1, block=False):
            
            if renpy.in_rollback():
                a = -a
                
            self.time = ramen.time + datetime.timedelta(hours=a)
            
            if self.time < self.start:
                self.time = self.start
                
            self.populate()

            if block:
                renpy.block_rollback()
            
            return self.time

        def nextday(self, a=8, block=True):
            b = 24 - self.time.hour
            
            if renpy.in_rollback():
                a = -a
                b = -b

            self.time = self.time + \
                datetime.timedelta(hours=b) + datetime.timedelta(hours=a)
            
            self.populate()
            
            if block:
                renpy.block_rollback()
                
            return self.time

        def populate(self):
            print "B"
            print ramen.time
            ramen.time = self.time
            print "S"
            print ramen.time

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
                
        def seed(self,what):
            if what == 'day':
                return self.time.strftime('%y%m%d')
            else:
                 return self.time.strftime('%U%j%H')
        
