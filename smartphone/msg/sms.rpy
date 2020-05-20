init -200 python:

    class ramen_messages(ramen_object):

        def __init__(self, id=None, **kwargs):
            self.makeid(id)
            self.kdict(**kwargs)
            self._msg = {}

        def newmsg(self, *args, **kwargs):

            msg = False

            if isinstance(args, (tuple, type([]))):
                if len(args) > 1:
                    msg_id = args[0]
                    msg = args[1]
                else:
                    msg_id = "sms_" + ramu.uid()
                    msg = args[0]
            else:
                msg_id = args

            try:
                msg_id
            except BaseException:
                msg_id = 'sms_' + ramu.uid()

            self._msg[msg_id] = object()

            self._msg[msg_id].__dict__ = kwargs

            if msg:
                self._msg[msg_id].content = msg

        def post(self, content, ref, val=None):
            msg_id = ramu.uid()
            self.newmsg(msg_id, content, ref=ref, sender='_mc')
            if val is not None:
                self.msg(ref, 'select', val)

        def msg(self, msg_id, attr=None, value=None):

            if value is not None and attr is not None:

                print msg_id
                print attr
                print value

                self._msg[msg_id].__dict__[attr] = value

                print self._msg[msg_id].__dict__[attr]

            if attr is None:
                try:
                    return self._msg[msg_id].__dict__
                except BaseException:
                    return False

            if value is None:
                try:
                    return self._msg[msg_id].__dict__[attr]
                except BaseException:
                    return None

        def refindex(self, msg_id):
            res = []
            for m in self._msg:
                try:
                    if self._msg[m].__dict__['ref'] == msg_id:
                        res.append(m)
                except BaseException:
                    pass
            if res == []:
                return False
            else:
                return res

        def delete(self, list):
            for i in list:
                del self._msg[i]

        def msgobj(self, msg_id):

            msg = object()
            msg.__dict__ = self.msg(msg_id).copy()

            try:
                msg.ref
            except BaseException:
                msg.ref = None
            try:
                msg.sender
            except BaseException:
                msg.sender = 'Unknown'
            try:
                msg.reply
            except BaseException:
                msg.reply = False

            try:
                msg.select
            except BaseException:
                msg.select = None

            if msg.sender == '_mc':
                msg.sender = mc_name

            return msg

init -20 python:

    sms = ramen_messages('sms')

    sms.newmsg('000', 'Cheap Loan! low interest. Call 5555-0912')
    sms.newmsg('m01', '[mc_name]? r u home?', sender='malika')
    sms.newmsg('m02', "at management office. why?", sender='_mc', ref='m01')
    sms.newmsg(
        'm03',
        "[mc_name]??",
        reply=[
            'You can come now.',
            'What?'],
        sender='malika')

    smphone.register('sms',
                     dir=ramu.getdir(),
                     title="SMS",
                     active=True,
                     order=8,
                     hcolor='#393'
                     )

screen smphone_apps_sms(var, page):

    python:
        app = ramu.makeobj(smphone.apps()['sms'])
        app.width = style['smphone_default_vbox'].xmaximum

    if page is None:
        use smphone_apps_sms_list(app, var, page)
    else:
        if var is None:
            use smphone_apps_sms_view(app, var, page)
        else:
            use smphone_apps_sms_reply(app, var, page)


screen smphone_apps_sms_list(app, var, page):

    use smphone_viewport(app.title, app.hcolor):

        style_prefix "sms"

        vbox:
            spacing 8

            for m in reversed(sorted(sms._msg)):
                $ msg = sms.msgobj(m)

                if msg.ref is None:
                    textbutton "{size=16}{color=#339}" + msg.sender.title() + "{/color}{/size}\n" + msg.content:
                        action SetScreenVariable('page', m)

screen smphone_apps_sms_reply(app, var, page):

    use smphone_viewport(app.title, app.hcolor):

        $ msg = sms.msgobj(page)

        vbox yfill True:
            spacing 8
            style_prefix "sms"

            vbox yalign 0.0:
                label msg.sender
                text msg.content

            vbox:
                spacing 8
                style_prefix "sms_reply"

                add ramu.hline((app.width, 1), "#999")
                label "Reply"

                for i in msg.reply:
                    $ s = msg.reply.index(i)
                    $ print s
                    textbutton i action[
                        Function(sms.post, content=i, ref=page, val=s),
                        SetScreenVariable('page', None),
                        SetScreenVariable('var', None),
                    ]

screen smphone_apps_sms_view(app, var, page):

    use smphone_viewport(app.title, app.hcolor):

        default reps = False

        $ msg = sms.msgobj(page)

        style_prefix "sms"
        vbox yfill True:
            spacing 8

            vbox yalign 0.0:
                label msg.sender
                text msg.content

            $ reps = sms.refindex(page)

            if reps:

                vbox yalign 1.0:
                    spacing 8
                    style_prefix 'sms_reply'

                    add ramu.hline((app.width, 1), "#999")
                    label "Reply"

                    for r in reps:
                        $ rep = sms.msgobj(r)
                        textbutton rep.content action SetScreenVariable('page', r):
                            xoffset 64
                            xsize style['smphone_default_vbox'].xmaximum - 72
                            text_align 1.0

            hbox yalign 1.0 xfill True:

                python:
                    dell = []
                    if reps:
                        dell = reps
                        dell.append(page)
                    else:
                        dell.append(page)

                style_prefix 'smphone_default'

                python:
                    try:
                        msg.select
                    except BaseException:
                        msg.select = None

                    if msg.select is None:
                        del_action = [
                            Function(
                                sms.delete, list=dell), SetScreenVariable(
                                'page', None)]
                    else:
                        del_action = None

                textbutton "{icon=trash-1}" action del_action

                textbutton "{icon=list}" action[
                    SetScreenVariable('page', None)
                ]

                if msg.reply and not reps:
                    textbutton "{icon=msg-reply}" action[
                        SetScreenVariable('var', True)
                    ]

                null width 2

style sms_text is ramen_tex:
    size 18
    color "#111"

style sms_button is button:
    padding(4, 4, 24, 4)
    xsize style['smphone_default_vbox'].xmaximum - 8
    background "#ddd"
    hover_background "#eee"
    insensitive_background "#ccc"

style sms_button_text is sms_text:
    color "#333"
    hover_color "#111"
    insensitive_color "#999"

style sms_reply_button is sms_button:
    background "#eee"
    padding(8, 8, 24, 8)

style sms_reply_button_text is sms_button_text:
    size 22
    xalign 1.0

style sms_label_text is ramen_tex:
    size 16
    color "#900"

style sms_reply_label:
    xalign 1.0

style sms_reply_label_text is ramen_tex:
    size 16
    color "#339"
