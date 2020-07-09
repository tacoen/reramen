init -400:

    style _console is _default:
        xpadding gui._scale(20)
        ypadding gui._scale(10)
        xfill True
        yfill True
        background "#111c"

    style _console_backdrop:
        background "#111c"

    style _console_vscrollbar is _vscrollbar

    style _console_text is _default:
        size gui._scale(16)

    style _console_input is _default:
        xfill True

    style _console_prompt is _console_text:
        minwidth gui._scale(22)
        text_align 1.0
        color "#eee"

    style _console_input_text is _console_text:
        color "#fff"
        adjust_spacing False
        caret Text("|", color="#fc3", size=14)

    style _console_history is _default:
        xfill True

    style _console_history_item is _default:
        xfill True
        bottom_margin gui._scale(8)

    style _console_command is _default:
        left_padding gui._scale(26)

    style _console_command_text is _console_text:
        color "#fff"

    style _console_result is _default:
        left_padding gui._scale(26)

    style _console_result_text is _console_text:
        color "#ccc"

    style _console_error_text is _console_text:
        color "#ccd"
        # color "#ff8080"

    style _console_trace is _default:
        background "#0001"
        xalign 1.0
        top_margin 20
        right_margin 20
        xpadding 2
        ypadding 2

    style _console_trace_text is _default:
        color "#fff"
        size gui._scale(16)

    style _console_trace_var is _console_trace_text:
        bold True
        color "#fff"

    style _console_trace_value is _console_trace_text

screen _console:
    # This screen takes as arguments:
    #
    # lines
    #    The current set of lines in the input buffer.
    # indent
    #    Indentation to apply to the new line.
    # history
    #    A list of command, result, is_error tuples.
    zorder 1500
    modal True
    layer 'console'

    if not _console.console.can_renpy():
        frame:
            style "_console_backdrop"

    frame:
        style "_console"

        has viewport:
            style_prefix "_console"
            mousewheel True
            scrollbars "vertical"
            yinitial 1.0

        has vbox

        # Draw historical console input.

        frame style "_console_history":

            has vbox:
                xfill True

            for he in history:

                frame style "_console_history_item":
                    has vbox

                    if he.command is not None:
                        frame style "_console_command":
                            xfill True
                            text "[he.command!q]" style "_console_command_text"

                    if he.result is not None:

                        frame style "_console_result":
                            if he.is_error:
                                text "[he.result!q]" style "_console_error_text"
                            else:
                                text "[he.result!q]" style "_console_result_text"

        # Draw the current input.
        frame style "_console_input":

            has vbox

            for line in lines:
                hbox:
                    spacing 4

                    if line[:1] != " ":
                        text "> " style "_console_prompt"
                    else:
                        text "... " style "_console_prompt"

                    text "[line!q]" style "_console_input_text"

            hbox:
                spacing 4

                if default[:1] != " ":
                    text "> " style "_console_prompt"
                else:
                    text "... " style "_console_prompt"

                input default default style "_console_input_text" exclude "" copypaste True

    key "game_menu" action Jump("_console_return")
    key "console_older" action _console.console.older
    key "console_newer" action _console.console.newer
