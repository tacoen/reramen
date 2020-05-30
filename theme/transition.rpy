init offset = -10

## Transitions ###########################################################
##
# These variables set transitions that are used when certain events occur.
# Each variable should be set to a transition, or None to indicate that no
# transition should be used.

# Entering or exiting the game menu.

define config.enter_transition = Pixellate(0.5, 4)
define config.exit_transition = Pixellate(0.5, 8)

# Between screens of the game menu.

define config.intra_transition =  Dissolve(.2)

# A transition that is used after a game has been loaded.

define config.after_load_transition = Dissolve(.2)

# Used when entering the main menu after the game has ended.

define config.end_game_transition = fade

# A variable to set the transition used when the game starts does not exist.
# Instead, use a with statement after showing the initial scene.

# Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
