##########################################################################
# Initialization
##########################################################################

# The init offset statement causes the initialization statements in this file
# to run before init statements in any other file.
init offset = -2


## Frames ################################################################
##
# These variables control the look of frames that can contain user interface
# components when an overlay or window is not present.

# Generic frames.
# define gui.frame_borders=Borders(4, 4, 4, 4)

# The frame that is used as part of the confirm screen.
# define gui.confirm_frame_borders=Borders(40, 40, 40, 40)

# The frame that is used as part of the skip screen.
# define gui.skip_frame_borders=Borders(16, 5, 50, 5)

# The frame that is used as part of the notify screen.
# define gui.notify_frame_borders=Borders(16, 5, 40, 5)

# Should frame backgrounds be tiled?
# define gui.frame_tile=False


## Bars, Scrollbars, and Sliders #########################################
##
# These control the look and size of bars, scrollbars, and sliders.
##
# The default GUI only uses sliders and vertical scrollbars. All of the other
# bars are only used in creator-written screens.

# The height of horizontal bars, scrollbars, and sliders. The width of vertical
# bars, scrollbars, and sliders.

# define gui.bar_size=25
# define gui.scrollbar_size=12
# define gui.slider_size=25

# True if bar images should be tiled. False if they should be linearly scaled.


# Horizontal borders.
# define gui.bar_borders=Borders(4, 4, 4, 4)
# define gui.scrollbar_borders=Borders(4, 4, 4, 4)
# define gui.slider_borders=Borders(4, 4, 4, 4)

# Vertical borders.
# define gui.vbar_borders=Borders(4, 4, 4, 4)
# define gui.vscrollbar_borders=Borders(4, 4, 4, 4)
# define gui.vslider_borders=Borders(4, 4, 4, 4)

# What to do with unscrollable scrollbars in the gui. "hide" hides them, while
# None shows them.


## NVL-Mode ##############################################################
##
# The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

# The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 10, 0, 20)

# The maximum number of NVL-mode entries Ren'Py will display. When more entries
# than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

# The height of an NVL-mode entry. Set this to None to have the entries
# dynamically adjust height.
define gui.nvl_height = 115

# The spacing between NVL-mode entries when gui.nvl_height is None, and between
# NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 10

# The position, width, and alignment of the label giving the name of the
# speaking character.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

# The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

# The position, width, and alignment of nvl_thought text (the text said by the
# nvl_narrator character.)
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

# The position of nvl menu_buttons.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

##########################################################################
# Mobile devices
##########################################################################

init python:

    # This increases the size of the quick buttons to make them easier to touch
    # on tablets and phones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(40, 14, 40, 0)

    # This changes the size and spacing of various GUI elements to ensure they
    # are easily visible on phones.
    if renpy.variant("small"):

        # Font sizes.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        # Adjust the location of the textbox.
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.text_xpos = 90
        gui.text_width = 1100

        # Change the size and spacing of various things.
        gui.slider_size = 36

        gui.choice_button_width = 1240

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        # File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        # NVL-mode.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
