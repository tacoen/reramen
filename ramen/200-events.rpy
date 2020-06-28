init -201 python:

    ramen.events = object()

    class ramen_event(object):

        def __init__(self, id, **kwargs):

            for k in kwargs:
                self.__dict__[str(k)] = kwargs[k]

            self.__dict__[str('id')] = str(id)

        def __call__(self):
            return self.__dict__

        def set(self, key, value):
            self.__dict__[key] = value

        def get(self, key):
            try:
                return self.__dict__[key]
            except BaseException:
                return None

        def __setattr__(self, key, value):
            self.set(key, value)

        def __getattr__(self, key):
            return self.get(key)

        def occur(self):

            if self.done:
                return False

            def are_gt(c, v, r=False):
                if c is None:
                    return None
                if float(v) >= float(c):
                    r=True
                return r

            def are_lt(c, v, r=False):
                if c is None:
                    return None
                if float(v) < float(c):
                    r=True
                return r

            def are_eq(c, v, r=False):
                if c is None:
                    return None
                if c == v:
                    r=True
                return r

            occur=[]

            print "masuk!"
            print self.__dict__

            if self.jump is None:
                return False

            else:

                t = are_gt(self.dayplay, ramentime.dayplay())
                if t is not None:
                    occur.append(t)

                t = are_eq(self.weekday, ramen.time.weekday())
                if t is not None:
                    occur.append(t)

                t = are_gt(self.hour_after, ramen.time.hour)
                if t is not None:
                    occur.append(t)

                t = are_lt(self.hour_before, ramen.time.hour)
                if t is not None:
                    occur.append(t)

                current_cond = []
                current_cond.append(ramentime.cond().lower())
                current_cond.append(ramentime.word().lower())
                current_cond.append(ramentime.ico().lower())

                print "----"
                print ramentime.word().lower()
                print current_cond

                if self.time_cond is not None:
                    if self.time_cond.lower() in current_cond:
                        occur.append(True)
                    else:
                        occur.append(False)

                t = are_gt(self.money_more, mc.money)
                if t is not None:
                    occur.append(t)

                t = are_lt(self.money_less, mc.money)
                if t is not None:
                    occur.append(t)

                t = are_gt(self.bank_more, mc.bank)
                if t is not None:
                    occur.append(t)

                t = are_lt(self.bank_less, mc.bank)
                if t is not None:
                    occur.append(t)

                if self.stat is not None:
                    for s in self.stat:
                        if mc.stat[s] >= self.stat[s]:
                            occur.append(True)
                        else:
                            occur.append(False)

                if self.skill is not None:
                    for s in self.skill:
                        if mc.job[s] >= self.skill[s]:
                            occur.append(True)
                        else:
                            occur.append(False)

                if renpy.has_label(self.jump):
                    occur.append(True)
                else:
                    occur.append(False)

            print occur

            if False in occur:
                return False
            else:
                return True

    def Event(id, done=False):
        """
        Return event from `ramen.events` by their id.

        if done is True: done attribute will added to the event

        """

        if done:
            ramen.events.__dict__[id].__dict__['done'] = True

        return ramen.events.__dict__[id]

    class define_event(object):
        """
        ``` python:
            define_event('joancall_0',
                label='home',
                dayplay=3,
                jump='joan.call'
                time_cond='night'
                money_more=200,
                stat={
                    'vital':8,
                    'hygiene':10
                }
                skill={
                    'it':5
                }
            )
        ```

        * event id = 'joancall_0' will occur when player reach 'home' label and jump to 'joan.call' label.
        * if meet this condition:
            * when 'night' after 3 days playing.
            * player has money >= 200
            * player has stat; vital at least 8, hygiene at least 10
            * player has skill; it at least 5

        * Yes, put more condition will made you game harder.
        * Note must put `Event('joancall_0',True)`, to made this event not repeating at 'joan.call' label
        * all event's label are jumped

        ### Keyword arguments

        | | Keyword | opr | Notes |
        | --- | --- | --- | --- |
        | | label | == | event triger label, use `ramen.label_last` |
        | Time | dayplay | > | after dayplay |
        | | weekday | == | At this weekday (decimal,where 0 is Sunday and 6 is Saturday.) |
        | | time_cond | == | see `pe.time_cond` |
        | | hour_after | >= | after this hour (decimal, 24H) |
        | | hour_before | < | before this hour (decimal, 24H) |
        | Score | money_less | < | has money(cash) less than this |
        | | money_more | >= | has money(cash) more than this |
        | | bank_less | < | has money in bank less than this |
        | | bank_more | >= | has money in bank more than this |
        | Attribute | stat | >= | at least has [what,value] |
        | | skill | >= | at least has [what,value] |
        | | has | == | having this in inventory [inventory,item] |


        """

        def __new__(cls, id=None, *args, **kwargs):

            if id is None:
                id = "event_" + str(ramu.uid())

            id = ramu.str_safe(id)
            ramen.events.__dict__[id] = ramen_event(id, **kwargs)
