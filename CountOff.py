import sublime
import sublime_plugin
import math

class CountOff(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        self.settings = sublime.load_settings('CountOff.sublime-settings')

    def run(self, edit):
        sels = self.view.sel()
        total_sels = len(sels)

        reverse_order = True if self.settings.get('reverse_order', False) is True else False
        include_zero = True if self.settings.get('include_zero', False) is True else False
        zero_fill = True if self.settings.get('zero_fill', False) is True else False

        pad_length = math.floor(math.log10(total_sels)) + 1 if zero_fill is True else 1

        if reverse_order:
            count = total_sels -1 if include_zero is True else total_sels
        else:
            count = 0 if include_zero is True else 1

        for sel in sels:
            if sel.empty():
                self.view.insert(edit, sel.begin(), str(count).rjust(pad_length, "0"))
                if reverse_order:
                    count -= 1
                else:
                    count += 1
