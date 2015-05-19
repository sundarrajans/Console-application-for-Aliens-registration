import os
import glob
import importlib
from os.path import basename, splitext 
__plugins_dir__=os.path.dirname(os.path.abspath(__file__))+"/plugins"
__pkg__="Aliens_on_Earth.plugins"
class Aliens(object):
    def __init__(self,details):
        self.code_name = details[0]
        self.blood_color=details[1]
        self.no_of_antennas=details[2]
        self.no_of_legs=details[3]
        self.home_planet=details[4]
    def __str__ (self):
        return self.code_name



def register(details,ui):
    ui = ui
    alien = Aliens(details)
    formt = get_user_format(ui)
    all_format = get_formats()
    if formt in all_format:
        mod=importlib.import_module("."+formt, __pkg__)
        format_plug = getattr(mod,formt)(alien)
        format_plug.create()
        return True
    else:
        ui.display("Invalid format")
        return False
    
def get_user_format(ui):
    ui.display('\n\nChoose any format\n')
    all_format = get_formats()
    input = ''
    for format in all_format:
        input += format+'\n'
    format =ui.prompt(input)
    return format

