init offset = -1

## Save directory ########################################################
# Windows: %APPDATA\RenPy\<config.save_directory>
# Macintosh: $HOME/Library/RenPy/<config.save_directory>
# Linux: $HOME/.renpy/<config.save_directory>
# This generally should not be changed, and if it is, should always be a
# literal string, not an expression.

define config.save_directory = "ramendir"

## Icon ##################################################################
##
# The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration ###################################################
##
# This section controls how Ren'Py turns your project into distribution files.

#init python:

    # The following functions take file patterns. File patterns are case-
    # insensitive, and matched against the path relative to the base directory,
    # with and without a leading /. If multiple patterns match, the first is
    # used.
    ##
    # In a pattern:
    ##
    # / is the directory separator.
    ##
    # * matches all characters, except the directory separator.
    ##
    # ** matches all characters, including the directory separator.
    ##
    # For example, "*.txt" matches txt files in the base directory, "game/
    # **.ogg" matches ogg files in the game directory or any of its
    # subdirectories, and "**.psd" matches psd files anywhere in the project.

    # Classify files as None to exclude them from the built distributions.


    # To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    # Files matching documentation patterns are duplicated in a mac app build,
    # so they appear in both the app and the zip file.




# A Google Play license key is required to download expansion files and perform
# in-app purchases. It can be found on the "Services & APIs" page of the Google
# Play developer console.

# define build.google_play_key = "..."


# The username and project name associated with an itch.io project, separated
# by a slash.

# define build.itch_project = "renpytom/test-project"



    