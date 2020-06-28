init -298 python:

    ramenpath= "E:/pp-renpy/ramen/"
    debuglog = "E:/pp-renpy/ramen/game/debug.txt"

    def dprint(text):
        file = open(debuglog, "a")
        file.writelines(text.strip())
        file.close()

    def jsondump(file, what):
        with open(file, 'w') as fp:
            json.dump(what, fp)

    jsondump(ramenpath+'ramu.txt', sorted(dir(ramu)))
