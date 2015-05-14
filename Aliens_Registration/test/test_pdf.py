from .. plugins import pdf
from . alien_mocker import Aliens

alien = Aliens()

def test_create():
    temp_format = pdf.pdf(alien)
    assert temp_format.create() == True
