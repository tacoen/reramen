init offset = -10

## Transitions ###########################################################
##
# These variables set transitions that are used when certain events occur.
# Each variable should be set to a transition, or None to indicate that no
# transition should be used.

# Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve

# Between screens of the game menu.

define config.intra_transition = dissolve


# A transition that is used after a game has been loaded.

define config.after_load_transition = None


# Used when entering the main menu after the game has ended.

define config.end_game_transition = None

# A variable to set the transition used when the game starts does not exist.
# Instead, use a with statement after showing the initial scene.

# Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


init -200:

    transform FadeInterval(ms=1.0):
        on show:
            alpha 0
            linear ms alpha 1
        on hide:
            alpha 1
            linear ms alpha 0

    transform delayed_blink(delay, cycle):
        alpha .5
        pause delay
        block:
            linear .2 alpha 1.0
            pause .2
            linear .2 alpha 0.5
            pause(cycle - .4)
            repeat

    transform ramen_lb:
        xalign 0.0
        yalign 1.0
        yoffset 24
