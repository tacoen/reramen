##########################################################################
# Initialization
##########################################################################

# init offset=-4

# style slider:
# ysize gui.slider_size
# base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
# thumb "gui/slider/horizontal_[prefix_]thumb.png"

# style vslider:
# xsize gui.slider_size
# base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
# thumb "gui/slider/vertical_[prefix_]thumb.png"

screen hbox_line(what, value, field_width=180, fa=0.0, va=1.0):

    hbox:
        text str(what) text_align fa xalign fa min_width field_width
        text str(value) text_align va xalign va

screen hbox_label(what, value, field_width=180, fa=0.0, va=1.0):

    hbox:
        label str(what):
            xsize field_width
            xalign fa
            text_xalign fa
            text_min_width field_width

        text str(value) text_align va xalign va xoffset 16
