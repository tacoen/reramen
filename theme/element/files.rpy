# The width and height of thumbnails used by the save slots.

define config.thumbnail_width = 256
define config.thumbnail_height = 144

# The number of columns and rows in the grid of save slots.


## Load and Save screens #################################################
##
# These screens are responsible for letting the player save the game and load
# it again. Since they share nearly everything in common, both are implemented
# in terms of a third screen, file_slots.
##
# https://www.renpy.org/doc/html/screen_special.html#save https://
# www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            # This ensures the input will get the enter event before any of the
            # buttons do.
            order_reverse True

            # The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            # The grid of file slots.
            grid pt.file_slot_cols pt.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing 12

                for i in range(pt.file_slot_cols * pt.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        frame background "#000" padding(0, 0, 0, 0):
                            add FileScreenshot(slot) xalign 0.5

                        null height 4

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            # Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing 8

                textbutton ico('chevrons-left') style 'page_arrow' text_size 20 action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                # range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton ico('chevrons-right') style 'page_arrow' action FilePageNext()

style page_label is ramen_label
style page_label_text is ramen_label_text

style page_button_text is ramen_gui

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color pt.hover_color

style page_button:
    padding(8, 8, 8, 8)
    hover_background "#0002"

style page_button_text is ramen_gui:
    size 24
    color  pt.small_color
    selected_color  pt.small_selected_color
    hover_color  pt.small_hover_color
    insensitive_color pt.small_insensitive_color

style page_arrow is ramen_icon:
    take page_button

style page_arrow_text is ramen_icon_text:
    take page_button_text
    line_leading 4
    size 22

style slot_button:
    xsize 276
    ysize 206
    xalign 0.5
    padding(10, 10, 10, 10)
    hover_background "#0002"

style slot_button_text is ramen_gui:
    take page_button_text
    size 14
    xalign 0.5

style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
