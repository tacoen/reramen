init -290 python:

    pt = ramen_persistent('theme')
    pt.about = []
    pt.about.append('32 Shades Theme by tacoen.itch.io')
    pt.about.append('Work Sans (C) Wei Huang. License OFL')
    pt.about.append('Abel (C) MADTypt. License OFL')

init -200 python:

    pt.nav_background = "#112"
    pt.notify_background = "#111D"

    pt.font_text = pe.theme_path + 'fonts/WorkSans-Regular.ttf'
    pt.font_label = pe.theme_path + 'fonts/WorkSans-SemiBold.ttf'
    pt.font_ui_title = pe.theme_path + 'fonts/WorkSans-ExtraLight.ttf'
    pt.font_ui_label = pe.theme_path + 'fonts/WorkSans-Light.ttf'
    pt.font_ui_text = pe.theme_path + 'fonts/Abel-Regular.ttf'
    pt.font_ui_ico = pe.theme_path + 'icons/fonts/feather-ramen2-icon.ttf'

    pt.accent_color = Color("#bbf")
    pt.idle_color = Color("#cce")
    pt.insensitive_color = Color(pt.idle_color).shade(0.7)
    pt.hover_color = Color("#ffe")
    pt.selected_color = '#fff'
    pt.text_color = '#ddd'

    pt.small_color = pt.idle_color
    pt.small_hover_color = Color(pt.small_color).tint(0.1)
    pt.small_selected_color = Color(pt.small_color).tint(0.7)
    pt.small_insensitive_color = pt.insensitive_color

    pt.overlays = pe.theme_path + 'gui/overlays'

    pt.hover_outlines = [(absolute(2), '#0006', absolute(0), absolute(0))]
    pt.idle_outlines = [(absolute(2), '#0003', absolute(0), absolute(0))]
    pt.insensitive_outlines = [
        (absolute(2), '#0000', absolute(0), absolute(0))]

    pt.dialoque_background = Color("#000").opacity(.75)
    pt.who_outlines = [
        (absolute(4),
         pt.dialoque_background,
         absolute(0),
         absolute(1))]

    pt.dialogue_text_xalign = 0.0
    pt.dialogue_width = config.screen_width / 2
    pt.dialogue_xpos = config.screen_width / 4 + 24
    pt.dialogue_ypos = 16

    pt.name_xalign = 0.0
    pt.name_xpos = pt.dialogue_xpos - 16
    pt.name_ypos = -24
    pt.name_size = 22
    pt.namebox_borders = (5, 5, 5, 5)
    pt.namebox_height = None
    pt.namebox_tile = False
    pt.namebox_width = None
    pt.textbox_height = config.screen_width / 7
    pt.textbox_yalign = 1.0

    pt.main_menu_background = pe.theme_path + "gui/main_background"
    pt.game_menu_background = pe.theme_path + "gui/game_background"

    pt.main_side_background = pe.theme_path + "gui/main_side"
    pt.game_side_background = pe.theme_path + "gui/game_side"

    pt.file_slot_cols = 3
    pt.file_slot_rows = 2

## default style #########################################################

    style['default'].language = 'unicode'

    style['frame'].background = Color('#0000')
    style['frame'].padding = (0, 0, 0, 0)

    style['input'].color = "#129"
    style['input'].adjust_spacing = False

    style['hyperlink_text'].color = "#9AB"
    style['hyperlink_text'].hover_underline = True
    style['hyperlink_text'].hover_color = "#ff0"

    style['button'].background = "#0000"
    style['button'].padding = (4, 4, 4, 4)
    style['button_text'].size = 20
    style['button_text'].yalign = 0.5

## ramen-theme #########################################################

init -199 python:

    style['bar'].ysize = 8
    style['bar'].right_bar = Color("#666")
    style['bar'].left_bar = Color("#666").tint(0.5)

    style['vbar'].xsize = 8
    style['vbar'].top_bar = Color("#666")
    style['vbar'].bottom_bar = Color("#666").tint(0.5)

    style['scrollbar'].ysize = 8
    style['scrollbar'].thumb = Color('#eee').opacity(.9)
    style['scrollbar'].base_bar = Color('#eee').opacity(.3)

    style['vscrollbar'].xsize = 8
    style['vscrollbar'].thumb = Color('#eee').opacity(.9)
    style['vscrollbar'].base_bar = Color('#eee').opacity(.3)

    style['ramen_icon'] = Style('button')

    style['hbox'] = Style('default')
    style['vbox'] = Style('default')

    style['ramen_icon_text'] = Style('default')
    style['ramen_icon_text'].font = pt.font_ui_ico
    style['ramen_icon_text'].antialias = True
    style['ramen_icon_text'].size = 32

    style['ramen_gui'] = Style('default')
    style['ramen_gui'].font = pt.font_ui_text
    style['ramen_gui'].antialias = True
    style['ramen_gui'].size = 24

    style['ramen_label'] = Style('ramen_gui')
    style['ramen_label_text'].color = pt.accent_color
    style['ramen_label_text'].size = 24
    style['ramen_label_text'].font = pt.font_ui_label

    style['ramen_tex'] = Style('default')
    style['ramen_tex'].font = pt.font_text
    style['ramen_tex'].antialias = True
    style['ramen_tex'].size = 24

    style['choice_button'] = Style('button')
    style['choice_button'].background = rui.button_frame(Color('#222'))
    style['choice_button'].hover_background = rui.button_frame(Color('#000'))
    style['choice_button'].insensitive_background = rui.button_frame(
        Color('#333').tint(.9))
    style['choice_button'].padding = (16, 12, 16, 12)
    style['choice_button'].xsize = 3 * (config.screen_width / 8)

    style['choice_button_text'] = Style('ramen_tex')
    style['choice_button_text'].font = pt.font_text
    style['choice_button_text'].size = 20
    style['choice_button_text'].insensitive_color = pt.insensitive_color
    style['choice_button_text'].color = pt.idle_color
    style['choice_button_text'].hover_color = Color('#fff')
    style['choice_button_text'].text_align = 0.5
    style['choice_button_text'].xalign = 0.5

    style['menu_start_button'] = Style('button')
    style['menu_start_button'].padding = (32, 12, 32, 12)
    style['menu_start_button'].background = Color(pt.nav_background)
    style['menu_start_button'].hover_background = Color(
        pt.nav_background).tint(.9)
    style['menu_start_button_text'] = Style('ramen_gui')
    style['menu_start_button_text'].size = 32

    style['menu_close_button'] = Style('button')
    style['menu_close_button'].padding = (12, 12, 12, 12)
    style['menu_close_button_text'] = Style('ramen_icon_text')
    style['menu_close_button_text'].size = 24
    style['menu_close_button_text'].color = pt.idle_color
    style['menu_close_button_text'].hover_color = '#fff'

    style['ramen_button'] = Style('button')
    style['ramen_button'].color = '#666'
    style['ramen_button'].padding = (8, 4, 8, 4)

    style['ramen_button_text'].size = 20
    style['ramen_button_text'].color = '#fff'
    style['ramen_button_text'].font = pt.font_ui_text
    style['ramen_button_text'].idle_color = Color(
        style['ramen_button_text'].color).opacity(.7)
    style['ramen_button_text'].hover_color = Color(
        style['ramen_button_text'].color).opacity(1)
    style['ramen_button_text'].selected_color = Color(
        style['ramen_button_text'].color).opacity(.7)
    style['ramen_button_text'].insensitive_color = Color(
        style['ramen_button_text'].color).opacity(.2)

    style['ramen_button_medium'] = Style('ramen_button')
    style['ramen_button_medium'].padding = (16, 8, 16, 8)
    style['ramen_button_medium_text'] = Style('ramen_button_text')
    style['ramen_button_medium_text'].size = 24

    style['ramen_button_large'] = Style('ramen_button')
    style['ramen_button_large'].padding = (32, 16, 32, 16)
    style['ramen_button_large_text'] = Style('ramen_button_text')
    style['ramen_button_large_text'].size = 32

    style['radio_button'] = Style('empty')
    style['radio_button'].left_padding = 32
    style['radio_button'].foreground = Text(
        ico('square'), font=pt.font_ui_ico, size=24, line_leading=4)
    style['radio_button'].selected_foreground = Text(
        ico('square-check'), font=pt.font_ui_ico, size=24, line_leading=4)

    style['check_button'] = Style('radio_button')
    style['check_button'].foreground = Text(
        ico('toggle-left'),
        font=pt.font_ui_ico,
        size=24,
        line_leading=4)
    style['check_button'].selected_foreground = Text(
        ico('toggle-right'), font=pt.font_ui_ico, size=24, line_leading=4)

    style['ramen_slider'] = Style('empty')
    style['ramen_slider'].ysize = 16
    style['ramen_slider'].padding = (0, 4, 0, 4)
    style['ramen_slider'].base_bar = Composite(
        (450, 16), (0, 7), Composite(
            (450, abs(3)), (0, 0), Solid('#fff3')))
    style['ramen_slider'].thumb = Text(
        ico('circle'), font=pt.font_ui_ico, size=16)

## etc ####################################################################

    config.narrator_menu = True
    config.history_length = 250
    config.window = "auto"

    preferences.text_cps = 0
    preferences.afm_time = 15
