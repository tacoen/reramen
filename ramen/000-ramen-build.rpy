
# must at last init

init python:

    build.include_old_themes  = False

    build.classify('**.rpy', None)

    build.classify('wiki/**', None)
    build.classify('game/doc/**', None)

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.md')
    build.documentation('*.html')
    build.documentation('*.txt')

    if not ramen.dev:

        build.archive('ramen-framework-'+config.version, "all")
        build.classify('game/ramen/**', 'ramen-framework-'+config.version )

        # exclude all developer script from the packages
        #build.classify('game/developer-option.*', None)
        build.classify('game/dev/**', None)

    if 'ramen_plugins_build' in dir():
        ramen_plugins_build()
