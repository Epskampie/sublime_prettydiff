# import sublime
import sublime_plugin
import subprocess
from sublime import Region


class PrettydiffBeautifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        # uri = edit.file_name()
        print('Prettydiff hello!', view.file_name())
        output = subprocess.check_output(
            'prettydiff ' +
            'mode:"beautify" ' +
            'readmethod:"filescreen" ' +
            'source:"' + view.file_name() + '" ',
            shell=True
        )
        output_string = output.decode('utf-8')
        print(output)
        view.replace(edit, Region(0, view.size()), output_string)
