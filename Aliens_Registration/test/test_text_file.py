from .. plugins import text_file
from . alien_mocker import Aliens

alien = Aliens()

def test_create():
    temp_format = text_file.text_file(alien)
    assert temp_format.create() == True
