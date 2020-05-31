init -80 python:

    import os.path
    from os import path

    class ramen_documentation():
        """ Create a md documentations from __doc__. base on pydoc but customized for renpy/ramen """

        def __init__(self, **kwagrs):

            self.dir = rds.md_path
            self.rs = ''
            self.files = filter(
                lambda w: w.endswith(".rpy"), sorted(
                    renpy.list_files(False)))

        def get_txtfile(self, file):

            sts = ''

            if path.exists(file):
                with open(file, 'r') as file:
                    sts = file.read()

            return sts

        def setting(self, **kwagrs):

            self.footer = "<small>Note This files created using ramen-dev makedoc() from working ramen ren'py project, same references may become a non existent.</small>" +\
                "\n\nMade with [[Ren'Py "+ renpy.version_only+ "|https://www.renpy.org/]]"

            self.title = 'Ramen'
            self.home_info = "Renpy according me, a modular approach. It is renpy framework to help you creating of visual novell game."

            self.report = ''

            try:
                for k in kwagrs(k):
                    self.__dict__[k] = kwagrs[k]
            except BaseException:
                pass

        def write(self, mdfile, sts):
            file = open(self.dir + mdfile + ".md", "w")
            file.writelines(self.wrapper(sts))
            file.close()
            self.rs += self.dir + mdfile + ".md -- created\n"

        def wrapper(self, sts=''):
            sts += "\n\n---\n\nGenerated Time: " + datetime.datetime.now().strftime('%c')
            sts += "\n\n" + self.footer
            sts = sts.replace('\n\n\n', '\n\n')
            return sts

        def collect_init(self, st=''):

            what = 'init'
            it = {}
            rep = ''

            for f in self.files:
                fn = ramu.file_info(f)
                c = ''
                pyh = ''
                rpy = ''
                sm = ''
                for line in open(rds.game_path + f, "r"):
                    line_fileinfo = fn.dir + "/" + fn.file
                    line = line.strip()
                    if line.startswith(what):
                        rn = line.split(what + ' ')
                        rn[1] = rn[1].replace(":", '')

                        if 'in' in rn[1]:
                            s = rn[1].split('in')
                            sm = s[1].strip()

                            line_fileinfo += " in " + sm

                            rn[1] = re.sub(r' in\s+.+', '', rn[1])

                        if 'python' in rn[1]:
                            v = rn[1].replace('python', '')
                            vs = str(v.strip())
                            if vs == "":
                                vs = '0'

                            try:
                                it[vs]
                            except BaseException:
                                it[vs] = {}
                            try:
                                it[vs]['python']
                            except BaseException:
                                it[vs]['python'] = []

                            it[vs]['python'].append(line_fileinfo.strip())

                        else:

                            v = rn[1].replace(' ', '')
                            if 'offset=' in v:
                                v = v.replace('offset=', '')
                            vs = str(v.strip())
                            if vs == "":
                                vs = '0'

                            try:
                                it[vs]
                            except BaseException:
                                it[vs] = {}
                            try:
                                it[vs]['renpy']
                            except BaseException:
                                it[vs]['renpy'] = []

                            it[vs]['renpy'].append(line_fileinfo.strip())

            list = it.keys()
            last = -10000
            list.sort(key=int)

            st = "# Init level\n\nRamen init level inspection\n\n"
            st += self.get_txtfile(rds.md_path+'txt/head-init.txt')
            st += "\n\n| level | code | file |\n| ---- | ---- | ---- |"

            rep = "\n\nInit Level:\n\n"

            for i in list:

                for w in ['python', 'renpy']:
                    try:
                        st += "\n|" + str(i) + "|" + w + "|"+ "<br>".join(it[str(i)][w]) +"|"
                        rep += "\n"+str(i) + "\t" + w + "\n\t\t"+ "\n\t\t". join(it[str(i)][w]) +"\n"

                    except BaseException:
                        pass

            self.write('ref_init_level', st + "\n\n")

            if rds.report:

                self.report += rep.replace("<br>", "\n\t\t\t")

        def collect_style(self):

            sts = "\n# Styles\n\n| file | list |\n| ---- | ---- |"

            for f in self.files:
                fn = ramu.file_info(f)
                line_fileinfo = fn.dir + "/" + fn.file
                c = []

                for line in open(rds.game_path + f, "r"):
                    line = line.strip()
                    if line.startswith(
                            'style') and '"' not in line and '=' not in line and '_prefix' not in line:
                        if ":" in line:
                            line = line[:-1]
                        line = line.replace('style ', '')
                        c.append(line)

                if not c == []:
                    sts += "\n| " + line_fileinfo + \
                        " | " + "<br>".join(c) + " |"

            self.write('ref_style', sts + "\n\n")

        def collect(self, what, st=''):

            st += "\n# " + what.title() + "\n\n"

            for f in self.files:
                fn = ramu.file_info(f)
                fine = True

                if what == 'label' and (
                        fn.path == 'element' or fn.name == 'screen'):
                    fine = False

                if fine:

                    line_fileinfo = "\n### " + \
                        fn.name + "\n\nFile: " + \
                        fn.dir + "/" + fn.file + "\n"
                    c = ''
                    for line in open(rds.game_path + f, "r"):
                        line = line.strip()

                        if "=" in line:
                            continue

                        if line.startswith(what):
                            rn = line.split(what + ' ')
                            try:
                                rn[1] = rn[1].replace(":", '')
                                c += "\n * " + rn[1]
                            except BaseException:
                                c += "\n * (!)" + line

                    if not c == '':
                        st += line_fileinfo + c + "\n"

            self.write("ref_"+what.lower(), st)

        def get_label(self):

            labels = sorted(list(renpy.get_all_labels()))
            files = ramu.files(False, False, '.rpy')
            last_file = ''
            st = ''

            for label in labels:

                if label.startswith('_'):
                    continue

                if "." in label:
                    s = label.split('.')
                    search_label = s[1]
                    word_label = "+--- "+ s[1] +" ("+label+")"
                else:
                    search_label = label
                    word_label = label

                for f in files:
                    if str(search_label)+":" in self.get_txtfile(rds.game_path+f):
                        if not f == last_file:
                            st +="\n\n"+f + " \n    "+ word_label+'\n'
                        else:
                            st +="    " + word_label+'\n'
                        break

                last_file = f

            ndx_st = self.get_txtfile(rds.md_path+'txt/head-label.txt')
            ndx_st += '# Labels\n\n'
            ndx_st += '```' + st + '\n```'
            self.write('ref_label', ndx_st)

            if rds.report:
                self.report += st

        def makereport(self):
            file = open( rds.game_path+"report.txt", "w" )
            rep = "Generated at : "+datetime.datetime.now().strftime('%c')+"\n"
            rep += self.report

            rep = re.sub(r'\n\n\n', '\n\n', rep)
            file.writelines(rep)
            file.close()

        def get_func(self):

            import sys
            import inspect

            collect = []

            ndx_st = self.get_txtfile(rds.md_path+'txt/head-func.txt')

            ndx_st += '# Non Class Function\n\n'

            for i in sorted(globals().keys()):
                o = globals()[i]
                try:
                    file = inspect.getfile(o)
                    if "game/" in file:

                        if inspect.isfunction(o):
                            ndx_st += "\n## " + i + "\n"
                            file = file.replace('game/', '')
                            ndx_st += "File: `" + file + "`\n"

                            try:
                                ndx_st += "\n  " + inspect.getdoc(o) + "\n"
                            except BaseException:
                                pass

                            ndx_st += "\n---\n"

                except BaseException:
                    pass

            self.write('ref_nonclassfunction', ndx_st)

        def getclass(self):

            import sys
            import inspect

            tag = ['container', 'ramen_time', 'event']
            cm = inspect.getmembers(sys.modules[__name__], inspect.isclass)
            ndx = []

            for c in cm:

                t1 = repr(c[1]) + repr(c[1].__bases__)

                if 'ramen' in t1 or c[0] in tag:

                    mdfile = 'class_' + str(c[0]).lower()
                    sts = "# " + str(c[0]) + "\n"

                    ndx.append('[[' + mdfile + ']]')

                    doc = inspect.getdoc(c[1])

                    try:
                        if 'ramen_' in str(c[1].__bases__):
                            gname = str(
                                c[1].__bases__).replace(
                                "(<class 'store.", '').replace(
                                "'>,)", '')
                            sts += "Base: [[class_" + gname + "]]\n"
                    except BaseException:
                        pass

                    if doc is not None:
                        sts += "\n" + str(doc).strip() + "\n\n"

                    for m in inspect.getmembers(c[1]):

                        if not m[0].startswith('__') or m[0] == "__init__":

                            try:
                                pr = inspect.getargspec(c[1].__dict__[m[0]])

                                if not m[0] == '__init__':
                                    # anchor = "(#"+c[0].lower()+"-"+
                                    # m[0].lower()+")"
                                    sts += "\n\n### " + m[0] + "\n"
                                else:
                                    sts += "### init\n"

                                if pr.defaults is not None:
                                    at = len(pr.args[1:]) - len(pr.defaults)
                                else:
                                    at = 0

                                if pr.keywords is not None:
                                    keywr = repr(pr.keywords).replace("'", "")
                                else:
                                    keywr = ""

                                ags = []
                                n = 0
                                cn = 0
                                d = ''
                                sp = ''
                                spa = '\n``` python\n'

                                if m[0] == '__init__':
                                    sp = "obj = " + str(c[0]) + "("
                                else:
                                    sp = "obj." + str(m[0]) + "("

                                for ag in pr.args[1:]:

                                    if n >= at:
                                        try:
                                            d = str(pr.defaults[cn])
                                        except BaseException:
                                            d = ""
                                        cn += 1

                                    if not d == "":
                                        sp += ag + "=" + d + ","
                                    else:
                                        sp += ag + ","

                                    n += 1

                                if not keywr == "":
                                    sp = sp + "**" + keywr

                                if sp.endswith(','):
                                    sp = sp[:-1]

                                sp = sp + ")"
                                spa += sp + "\n```\n\n"

                                sts += "\n\n*Syntax and default parameters:*\n" + spa

                                try:
                                    doc = inspect.getdoc(c[1].__dict__[m[0]])
                                    if doc is not None:
                                        sts += str(doc).strip() + "\n"
                                except BaseException:
                                    pass

                            except BaseException:
                                pass

                    self.write(mdfile, sts)

            return ndx

        def geth1(self, mdfile):
            title = []
            for line in open(mdfile, "r"):
                line.strip()
                if line.startswith('# '):
                    line = line.replace('# ', '')
                    line = line.rstrip()
                    if line.endswith(':'):
                        line = line.replace(':', '')
                    title.append(line)

            return title

        def mdindex(self, what, st=''):
            import glob

            files = glob.glob(self.dir +'txt/'+ what + "*.txt")

            for f in files:
                fn = ramu.file_info(f)
                fn.md = fn.file.replace('.txt', '.md').replace('/txt', '')
                #mdfile = fn.name+ suffix
                title = self.geth1(f)
                st += " * [[" + str(title[0]) + "|" + fn.name + "]]\n"

                sts = self.get_txtfile(f)

                self.write(fn.name, sts)

            return st

        def class_index(self, filename, ndx, ndx_st='', footer=''):
            for n in sorted(ndx):
                md = n.replace('[[', '').replace(']]', '')
                title = self.geth1(rds.md_path + md + ".md")
                ndx_st += " * [[" + title[0] + "|" + md + "]]\n"
            self.write(filename, ndx_st + footer)

        def build(self, rprint=True):

            self.rs = ''

            self.setting()

        # class
            ndx = self.getclass()
            self.class_index('class_index', ndx, "# Class Index\n\n")

            self.get_func()
            self.get_label()

            self.collect('screen')
            self.collect('transform')
            self.collect_style()

            self.collect_init()

        # home

            home = "# " + self.title + "\n\n"
            home += "\n" + self.home_info + "\n\n"

            home += "## Reference:\n\n"
            home += " * [[Class Index|class_index]]\n"
            home += " * [[Non Class Functions|ref_nonclassfunction]]\n"
            home += " * [[Screens|ref_screen]]\n"
            home += " * [[Styles|ref_style]]\n"
            home += " * [[Labels|ref_label]]\n"
            home += " * [[Transform|ref_transform]]\n"
            home += " * [[Init level|ref_init_level]]\n"

            for t in ['tips', 'howto', 'snip', 'info']:

                stp = t.title()
                if t == 'snip':
                    stp = 'Snipset'

                home += "\n## " + stp + "\n\n"
                home += self.mdindex(t)
                home += "\n"

            self.write('index', home)

            if rds.report:
                self.makereport()

            if rprint:
                print self.rs
            else:
                return self.rs

    ramendoc = ramen_documentation()

init offset = -2

screen rdsa_tools_md():
    $ report = ramendoc.build(False)
    text report style 'ramen_gui'
