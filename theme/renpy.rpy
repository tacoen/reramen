init -305 python:

    # avoid rebuild, gui.init must in early init level
    # this supply config.screen_width and config.screen_height, etc
    # which are used in theme making and many function

    gui.init(1280, 720)

init -5 python:

    # needed

    gui.button_tile = False
    gui.bar_tile = False
    gui.scrollbar_tile = False
    gui.slider_tile = False
    gui.unscrollable = "hide"

    gui.button_borders = Borders(4, 4, 4, 4)

    # This determines history screen.

    gui.history_allow_tags = set()
    gui.history_height = 32

    # please confirm:

    gui.accent_color = pt.accent_color
    gui.idle_color = pt.idle_color
    gui.insensitive_color = pt.insensitive_color
    gui.hover_color = pt.hover_color
    gui.selected_color = pt.selected_color
    gui.text_color = pt.text_color
    gui.interface_text_color = pt.text_color

#    gui.muted_color='#002851'
#    gui.hover_muted_color='#003d7a'

    gui.text_font = pt.font_text
    gui.interface_text_font = pt.font_ui_text
    gui.text_size = 22
    gui.interface_text_size = 20
    gui.label_text_size = 22
    gui.notify_text_size = 16
    gui.title_text_size = 48

    gui.name_text_font = pt.font_label
    gui.name_text_size = 24
