import os
from .. import admin
from .mock_ui import Ui
from .alien_mocker import Aliens 
from .plugin_mocker import temp_format
def test_Aliens():
    details = ('test_name',' test_color','1','2','test_planet')
    alien = admin.Aliens(details)
    assert alien.code_name == 'test_name'
    assert alien.home_planet == 'test_planet'


def test_get_format():
    __plugins_dir__=os.path.dirname(os.path.abspath(__file__))+"/plugins"
    assert admin.get_formats () == ['pdf','text_file']

def test_get_user_format():
    ui = Ui()
    assert admin.get_user_format(ui) == "Test_format"
    
def test_register():
    ui= Ui()
    admin.Aliens = Aliens
    details=("test")
    admin.register.format_plug =  temp_format
    admin.register(details,ui) 
